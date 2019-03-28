from fontbakery.fonts_profile import profile_factory  # NOQA pylint: disable=unused-import
from fontbakery.checkrunner import Section

OPENTYPE_PROFILE_IMPORTS = (
    ".",
    (
        "cmap",
        "head",
        "os2",
        "post",
        "name",
        "loca",
        "hhea",
        "dsig",
        "hmtx",
        "gpos",
        "kern",
        "glyf",
        "fvar",
        "shared_conditions",
    ),
)
profile_imports = (OPENTYPE_PROFILE_IMPORTS, )
profile = profile_factory(default_section=Section("OpenType Specification Checks"))

OPENTYPE_PROFILE_CHECKS = [
    'com.google.fonts/check/family/underline_thickness',
    'com.google.fonts/check/family/panose_proportion',
    'com.google.fonts/check/family/panose_familytype',
    'com.google.fonts/check/family/equal_unicode_encodings',
    'com.google.fonts/check/family/equal_font_versions',
    'com.adobe.fonts/check/family/bold_italic_unique_for_nameid1',
    'com.adobe.fonts/check/family/max_4_fonts_per_family_name',
    'com.adobe.fonts/check/name/postscript_vs_cff',
    'com.adobe.fonts/check/name/postscript_name_consistency',
    'com.adobe.fonts/check/name/empty_records',
    'com.google.fonts/check/name/no_copyright_on_description',
    'com.google.fonts/check/name/line_breaks',
    'com.google.fonts/check/name/rfn',
    'com.google.fonts/check/name/match_familyname_fullfont',
    'com.google.fonts/check/varfont/regular_wght_coord',
    'com.google.fonts/check/varfont/regular_wdth_coord',
    'com.google.fonts/check/varfont/regular_slnt_coord',
    'com.google.fonts/check/varfont/regular_ital_coord',
    'com.google.fonts/check/varfont/regular_opsz_coord',
    'com.google.fonts/check/varfont/bold_wght_coord',
    'com.google.fonts/check/loca/maxp_num_glyphs',
    'com.google.fonts/check/font_version',
    'com.google.fonts/check/post_table_version',
    'com.google.fonts/check/monospace',
    'com.google.fonts/check/xavgcharwidth',
    'com.adobe.fonts/check/fsselection_matches_macstyle',
    'com.google.fonts/check/linegaps',
    'com.google.fonts/check/unitsperem',
    'com.google.fonts/check/dsig',
    'com.google.fonts/check/whitespace_widths',
    'com.google.fonts/check/gpos_kerning_info',
    'com.google.fonts/check/kern_table',
    'com.google.fonts/check/glyf_unused_data',
    'com.google.fonts/check/family_naming_recommendations',
    'com.google.fonts/check/maxadvancewidth',
    'com.google.fonts/check/points_out_of_bounds',
    'com.google.fonts/check/all_glyphs_have_codepoints',
    'com.google.fonts/check/monospace_max_advancewidth',
    'com.google.fonts/check/wght_valid_range'
]

profile.auto_register(globals())
profile.test_expected_checks(OPENTYPE_PROFILE_CHECKS, exclusive=True)
