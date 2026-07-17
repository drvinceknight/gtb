"""Colourblind-safety guard for the diagram palette.

The three data colours in ``tex/gtbtikz.tex`` are used in the evolutionary
biology and numerical integration diagrams, where colour carries meaning
(genotype versus phenotype versus fitness, and so on). They were chosen to stay
distinguishable from each other, and from the grey panel, under simulated
colour vision deficiencies. This test parses those colours straight from the
style file and checks that property, so a later tweak to a hex value cannot
silently reintroduce a palette that fails for colourblind readers.
"""

import itertools
import pathlib
import re

import pytest

STYLE_FILE = (
    pathlib.Path(__file__).resolve().parent.parent / "tex" / "gtbtikz.tex"
)

# The verified trio, plus the canvas they sit on.
DATA_COLOUR_NAMES = ["gtbblue", "gtbterracotta", "gtbyellow"]
CANVAS_NAME = "gtbcanvas"

# Worst-case CAM02-UCS separation must clear these. The trio scores about 34
# between colours and about 27 against the canvas; the Okabe-Ito palette it
# replaced scored only 11.7 between colours, so these thresholds keep the new
# palette comfortably better than the baseline without being brittle.
MIN_PAIR_SEPARATION = 25.0
MIN_CANVAS_SEPARATION = 20.0

CVD_TYPES = ["deuteranomaly", "protanomaly", "tritanomaly"]


def parse_colour(name):
    """Read a ``\\definecolor{name}{HTML}{RRGGBB}`` value from the style file."""
    text = STYLE_FILE.read_text()
    match = re.search(
        r"\\definecolor\{" + re.escape(name) + r"\}\{HTML\}\{([0-9A-Fa-f]{6})\}",
        text,
    )
    if match is None:
        raise AssertionError(f"colour {name!r} not found in {STYLE_FILE}")
    value = match.group(1)
    return [int(value[index : index + 2], 16) / 255.0 for index in (0, 2, 4)]


def simulate(rgb, cvd_type):
    from colorspacious import cspace_convert

    if cvd_type is None:
        return rgb
    space = {"name": "sRGB1+CVD", "cvd_type": cvd_type, "severity": 100}
    converted = cspace_convert(rgb, space, "sRGB1")
    return [min(1.0, max(0.0, channel)) for channel in converted]


def separation(first, second, cvd_type):
    from colorspacious import deltaE

    return deltaE(
        simulate(first, cvd_type),
        simulate(second, cvd_type),
        input_space="sRGB1",
        uniform_space="CAM02-UCS",
    )


@pytest.mark.parametrize("cvd_type", [None] + CVD_TYPES)
def test_data_colours_separated_from_each_other(cvd_type):
    """Every pair of data colours stays distinct under each condition."""
    pytest.importorskip("colorspacious")
    colours = [parse_colour(name) for name in DATA_COLOUR_NAMES]
    for (first, name_first), (second, name_second) in itertools.combinations(
        zip(colours, DATA_COLOUR_NAMES), 2
    ):
        distance = separation(first, second, cvd_type)
        condition = cvd_type or "normal vision"
        assert distance >= MIN_PAIR_SEPARATION, (
            f"{name_first} and {name_second} are too close under {condition}: "
            f"dE = {distance:.1f} < {MIN_PAIR_SEPARATION}"
        )


@pytest.mark.parametrize("cvd_type", [None] + CVD_TYPES)
def test_data_colours_separated_from_canvas(cvd_type):
    """Every data colour stays legible against the grey panel."""
    pytest.importorskip("colorspacious")
    canvas = parse_colour(CANVAS_NAME)
    for name in DATA_COLOUR_NAMES:
        distance = separation(parse_colour(name), canvas, cvd_type)
        condition = cvd_type or "normal vision"
        assert distance >= MIN_CANVAS_SEPARATION, (
            f"{name} is too close to the canvas under {condition}: "
            f"dE = {distance:.1f} < {MIN_CANVAS_SEPARATION}"
        )
