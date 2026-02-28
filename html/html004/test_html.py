
import pytest
from bs4 import BeautifulSoup
import cssutils

@pytest.fixture(scope="module")
def html_soup():
    with open("index.html", encoding="utf-8") as f:
        return BeautifulSoup(f, "html.parser")

@pytest.fixture(scope="module")
def css_rules():
    with open("style.css", encoding="utf-8") as f:
        sheet = cssutils.parseString(f.read())
    return {rule.selectorText: {prop.name: prop.value for prop in rule.style}
            for rule in sheet if rule.type == rule.STYLE_RULE}

# 1-10: 1 pontos feladatok

def test_1_body_styles(css_rules):
    body = css_rules.get("body", {})
    assert body.get("font-family", "").startswith("Arial")
    assert body.get("background-color") == "#FAFAFA"
    assert body.get("color") == "#222"

def test_2_body_margin_padding(css_rules):
    body = css_rules.get("body", {})
    assert body.get("margin") == "0"
    assert body.get("padding") == "0"

def test_3_container(css_rules):
    container = css_rules.get(".container", {})
    assert container.get("width") == "85%"
    assert container.get("margin") == "0 auto"

def test_4_header_flex(css_rules):
    header = css_rules.get("header", {})
    assert header.get("display") == "flex"
    assert "align-items" in header

def test_5_logo_max_width(css_rules):
    logo = css_rules.get(".logo", {})
    assert logo.get("max-width") == "100px"

def test_6_h1_font_size(css_rules):
    h1 = css_rules.get("h1", {})
    assert h1.get("font-size") == "2.5em"

def test_7_hr_style(css_rules):
    hr = css_rules.get(".kek-vonal", {})
    assert hr.get("height") == "4px"
    assert hr.get("background-color") == "#09F"
    assert hr.get("border") == "none"

def test_8_motto_italic(css_rules):
    motto = css_rules.get(".motto", {})
    assert motto.get("font-style") == "italic"

def test_9_helyszin_center(css_rules):
    helyszin = css_rules.get(".helyszin", {})
    assert helyszin.get("text-align") == "center"

def test_10_footer_center(css_rules):
    footer = css_rules.get("footer", {})
    assert footer.get("text-align") == "center"

# 11-25: 2 pontos feladatok

def test_11_navmenu_flex(css_rules):
    nav = css_rules.get(".navmenu", {})
    assert nav.get("display") == "flex"
    assert nav.get("justify-content") == "center"
    assert nav.get("gap") == "20px"

def test_11_2(css_rules):
    test_11_navmenu_flex(css_rules)

def test_12_program_margin(css_rules):
    program = css_rules.get(".program", {})
    assert program.get("margin") == "40px 0"

def test_12_2(css_rules):
    test_12_program_margin(css_rules)

def test_13_eloadok_flex(css_rules):
    eloadok = css_rules.get(".eloadok-lista", {})
    assert eloadok.get("display") == "flex"
    assert eloadok.get("justify-content") == "space-between"

def test_13_2(css_rules):
    test_13_eloadok_flex(css_rules)

def test_14_article_width(css_rules):
    article = css_rules.get(".eloadok-lista article", {})
    assert article.get("width") == "30%"

def test_14_2(css_rules):
    test_14_article_width(css_rules)

def test_15_img_size(css_rules):
    img = css_rules.get(".eloadok-lista img", {})
    assert img.get("width") == "150px"
    assert img.get("height") == "auto"

def test_15_2(css_rules):
    test_15_img_size(css_rules)

def test_16_h4_style(css_rules):
    h4 = css_rules.get(".eloadok-lista h4", {})
    assert h4.get("font-weight") == "bold"
    assert h4.get("font-size") == "20px"
    assert h4.get("margin") == "10px 0 5px"

def test_16_2(css_rules):
    test_16_h4_style(css_rules)

def test_17_article_text_center(css_rules):
    article = css_rules.get(".eloadok-lista article", {})
    assert article.get("text-align") == "center"

def test_17_2(css_rules):
    test_17_article_text_center(css_rules)

def test_18_img_border_radius(css_rules):
    img = css_rules.get(".eloadok-lista img", {})
    assert img.get("border-radius") == "10px"

def test_18_2(css_rules):
    test_18_img_border_radius(css_rules)

def test_19_section_spacing(css_rules):
    sections = css_rules.get("section", {})
    assert "margin-top" in sections or "margin" in sections

def test_19_2(css_rules):
    test_19_section_spacing(css_rules)

def test_20_motto_styling(css_rules):
    assert css_rules.get(".motto", {}).get("font-style") == "italic"

def test_20_2(css_rules):
    test_20_motto_styling(css_rules)
