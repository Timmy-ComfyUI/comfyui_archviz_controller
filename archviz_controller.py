"""
ARCHVIZ CONTROLLER
============================

Workflow-specific controller for the Architecture & Landscape presets.

Controls:
    1.  Use Manual Prompt?
    2.  Environment
    3.  Interior Lighting
    4.  Interior Composition
    5.  Interior Lens
    6.  Exterior Lighting
    7.  Exterior Composition
    8.  Exterior Lens
    9.  Landscape Lighting
    10. Landscape Composition
    11. Landscape Lens
    12. Seed
    13. Aspect Ratio
    14. Megapixels

The actual preset text remains inside the ComfyUI workflow.
Dropdowns are converted to integer selector values for Dazzle Switches.

Dazzle Switch selector convention:
    0 = normal/manual selection
    1 = input_01
    2 = input_02
    3 = input_03
    etc.
"""

from __future__ import annotations


class ARCHVIZ_CONTROLLER:
    """Central controller for the ArchViz presets."""

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {

                # -----------------------------------------------------
                # 1. PROMPT CONTROL
                # -----------------------------------------------------

                "use_manual_prompt": (
                    "BOOLEAN",
                    {"default": False}
                ),

                # -----------------------------------------------------
                # 2. ENVIRONMENT
                # -----------------------------------------------------

                "environment": (
                    [
                        "Interior",
                        "Exterior",
                        "Landscape",
                    ],
                    {"default": "Interior"}
                ),

                # -----------------------------------------------------
                # 3. INTERIOR PRESETS
                # -----------------------------------------------------

                "interior_lighting": (
                    [
                        "Soft Daylight",
                        "Direct Sunlight",
                        "Warm Evening",
                        "Dramatic Directional",
                    ],
                    {"default": "Soft Daylight"}
                ),

                "interior_composition": (
                    [
                        "Wide",
                        "Editorial",
                        "Detail",
                    ],
                    {"default": "Wide"}
                ),

                "interior_lens": (
                    [
                        "24mm",
                        "35mm",
                        "50mm",
                    ],
                    {"default": "24mm"}
                ),

                # -----------------------------------------------------
                # 4. EXTERIOR PRESETS
                # -----------------------------------------------------

                "exterior_lighting": (
                    [
                        "Overcast Daylight",
                        "Direct Sunlight",
                        "Golden Hour",
                        "Blue Hour",
                    ],
                    {"default": "Overcast Daylight"}
                ),

                "exterior_composition": (
                    [
                        "Wide",
                        "Editorial",
                        "Detail",
                    ],
                    {"default": "Wide"}
                ),

                "exterior_lens": (
                    [
                        "24mm",
                        "35mm",
                        "50mm",
                    ],
                    {"default": "24mm"}
                ),

                # -----------------------------------------------------
                # 5. LANDSCAPE PRESETS
                # -----------------------------------------------------

                "landscape_lighting": (
                    [
                        "Soft Daylight",
                        "Direct Sunlight",
                        "Golden Hour",
                        "Mist & Atmosphere",
                    ],
                    {"default": "Soft Daylight"}
                ),

                "landscape_composition": (
                    [
                        "Wide",
                        "Layered",
                        "Detail",
                    ],
                    {"default": "Wide"}
                ),

                "landscape_lens": (
                    [
                        "24mm",
                        "50mm",
                        "85mm",
                    ],
                    {"default": "24mm"}
                ),

                # -----------------------------------------------------
                # 6. SEED
                # -----------------------------------------------------

                "seed": (
                    "INT",
                    {
                        "default": 0,
                        "min": 0,
                        "max": 0xFFFFFFFFFFFFFFFF,
                        "step": 1,
                        "control_after_generate": True,
                    }
                ),

                # -----------------------------------------------------
                # 7. ASPECT RATIO
                # -----------------------------------------------------

                "aspect_ratio": (
                    [
                        "1:1 (Square)",
                        "2:3 (Portrait Photo)",
                        "3:2 (Photo)",
                        "3:4 (Portrait Standard)",
                        "4:3 (Standard)",
                        "9:16 (Portrait Widescreen)",
                        "16:9 (Widescreen)",
                        "21:9 (Ultrawide)",
                    ],
                    {"default": "2:3 (Portrait Photo)"}
                ),

                # -----------------------------------------------------
                # 8. MEGAPIXELS
                # -----------------------------------------------------

                "megapixels": (
                    "FLOAT",
                    {
                        "default": 1.0,
                        "min": 0.1,
                        "max": 16.0,
                        "step": 0.1,
                        "round": 0.1,
                    }
                ),
            }
        }

    # ---------------------------------------------------------------
    # OUTPUT TYPES
    # ---------------------------------------------------------------

    RETURN_TYPES = (
        "BOOLEAN",  # 0  use_manual_prompt

        "INT",      # 1  environment
        "INT",      # 2  interior_lighting
        "INT",      # 3  interior_composition
        "INT",      # 4  interior_lens

        "INT",      # 5  exterior_lighting
        "INT",      # 6  exterior_composition
        "INT",      # 7  exterior_lens

        "INT",      # 8  landscape_lighting
        "INT",      # 9  landscape_composition
        "INT",      # 10 landscape_lens

        "INT",      # 11 seed
        "*",        # 12 aspect_ratio
        "FLOAT",    # 13 megapixels
    )

    # ---------------------------------------------------------------
    # OUTPUT NAMES
    # ---------------------------------------------------------------

    RETURN_NAMES = (
        "use_manual_prompt",

        "environment",
        "interior_lighting",
        "interior_composition",
        "interior_lens",

        "exterior_lighting",
        "exterior_composition",
        "exterior_lens",

        "landscape_lighting",
        "landscape_composition",
        "landscape_lens",

        "seed",
        "aspect_ratio",
        "megapixels",
    )

    FUNCTION = "execute"

    CATEGORY = "ArchViz"

    # ---------------------------------------------------------------
    # EXECUTION
    # ---------------------------------------------------------------

    def execute(
        self,
        use_manual_prompt,

        environment,
        interior_lighting,
        interior_composition,
        interior_lens,

        exterior_lighting,
        exterior_composition,
        exterior_lens,

        landscape_lighting,
        landscape_composition,
        landscape_lens,

        seed,
        aspect_ratio,
        megapixels,
    ):
        """Convert dropdown selections to Dazzle Switch selector values."""

        # Environment selector
        environments = {
            "Interior": 1,
            "Exterior": 2,
            "Landscape": 3,
        }

        # Interior selectors
        interior_lightings = {
            "Soft Daylight": 1,
            "Direct Sunlight": 2,
            "Warm Evening": 3,
            "Dramatic Directional": 4,
        }

        interior_compositions = {
            "Wide": 1,
            "Editorial": 2,
            "Detail": 3,
        }

        interior_lenses = {
            "24mm": 1,
            "35mm": 2,
            "50mm": 3,
        }

        # Exterior selectors
        exterior_lightings = {
            "Overcast Daylight": 1,
            "Direct Sunlight": 2,
            "Golden Hour": 3,
            "Blue Hour": 4,
        }

        exterior_compositions = {
            "Wide": 1,
            "Editorial": 2,
            "Detail": 3,
        }

        exterior_lenses = {
            "24mm": 1,
            "35mm": 2,
            "50mm": 3,
        }

        # Landscape selectors
        landscape_lightings = {
            "Soft Daylight": 1,
            "Direct Sunlight": 2,
            "Golden Hour": 3,
            "Mist & Atmosphere": 4,
        }

        landscape_compositions = {
            "Wide": 1,
            "Layered": 2,
            "Detail": 3,
        }

        landscape_lenses = {
            "24mm": 1,
            "50mm": 2,
            "85mm": 3,
        }

        return (
            use_manual_prompt,

            environments[environment],
            interior_lightings[interior_lighting],
            interior_compositions[interior_composition],
            interior_lenses[interior_lens],

            exterior_lightings[exterior_lighting],
            exterior_compositions[exterior_composition],
            exterior_lenses[exterior_lens],

            landscape_lightings[landscape_lighting],
            landscape_compositions[landscape_composition],
            landscape_lenses[landscape_lens],

            seed,
            aspect_ratio,
            megapixels,
        )


# -------------------------------------------------------------------
# COMFYUI REGISTRATION
# -------------------------------------------------------------------

NODE_CLASS_MAPPINGS = {
    "ARCHVIZ_CONTROLLER": ARCHVIZ_CONTROLLER,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ARCHVIZ_CONTROLLER": "ArchViz Controller",
}
