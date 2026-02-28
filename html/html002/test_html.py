
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
        return cssutils.parseString(f.read())

def get_style_for_selector(sheet, selector):
    for rule in sheet:
        if rule.type == rule.STYLE_RULE and rule.selectorText == selector:
            return {p.name: p.value for p in rule.style}
    return {}

def rule_exists(sheet, selector, property_name, value):
    styles = get_style_for_selector(sheet, selector)
    return styles.get(property_name) == value

# 1. Háttér- és szövegszín
def test_feladat_1(css_rules):
    assert rule_exists(css_rules, "body", "background-color", "#F0F0F0")
    assert rule_exists(css_rules, "body", "color", "#333")

# 2. Arial betűtípus
def test_feladat_2(css_rules):
    styles = get_style_for_selector(css_rules, "body")
    assert "arial" in styles.get("font-family", "").lower()

# 3. Margin/padding 0
def test_feladat_3(css_rules):
    styles = get_style_for_selector(css_rules, "body")
    assert styles.get("margin") == "0"
    assert styles.get("padding") == "0"

# 4. .keret szélesség és középre
def test_feladat_4(css_rules):
    styles = get_style_for_selector(css_rules, ".keret")
    assert styles.get("width") == "90%"
    assert styles.get("margin") == "0 auto"

# 5. .keret > * margó
def test_feladat_5(css_rules):
    styles = get_style_for_selector(css_rules, ".keret > *")
    assert styles.get("margin-bottom") == "50px" or styles.get("margin-top") == "50px"

# 6. fejezet2 középre
def test_feladat_6(css_rules):
    styles = get_style_for_selector(css_rules, "h2")
    assert styles.get("text-align") == "center"

# 7. hr stílus
def test_feladat_7(css_rules):
    styles = get_style_for_selector(css_rules, "hr")
    assert styles.get("height") == "3px"
    assert styles.get("background-color") == "#CCC"
    assert styles.get("border") == "none"

# 8. Kép szélessége
def test_feladat_8(css_rules):
    styles = get_style_for_selector(css_rules, "img")
    assert styles.get("width") == "300px"

# 9. Kép lekerekítés
def test_feladat_9(css_rules):
    styles = get_style_for_selector(css_rules, "img")
    assert styles.get("border-radius") == "10px"

# 10. Lábléc középre
def test_feladat_10(css_rules):
    styles = get_style_for_selector(css_rules, "footer")
    assert styles.get("text-align") == "center"

# 11. h1 tartalma
def test_feladat_11(html_soup):
    h1 = html_soup.find("h1")
    assert h1 is not None
    assert h1.text.strip() == "Iskolaudvar"

    h1 = html_soup.find("h1")
    assert h1 is not None and "Iskolaudvar" in h1.text

def test_feladat_11_2(html_soup):
    test_feladat_11(html_soup)

# 12. bemutato szakasz felépítése
def test_feladat_12(html_soup):
    szakasz = html_soup.find("div", class_="bemutato")
    assert szakasz is not None
    assert szakasz.find("h2") and szakasz.find("p")

def test_feladat_12_2(html_soup):
    test_feladat_12(html_soup)

# 13. bekezdes dőlt
def test_feladat_13(css_rules):
    styles = get_style_for_selector(css_rules, ".bemutato > p")
    assert styles.get("font-style") == "italic"

def test_feladat_13_2(css_rules):
    test_feladat_13(css_rules)

# 14. hr a bemutato után
def test_feladat_14(html_soup):
    szakasz = html_soup.find("div", class_="bemutato")
    assert szakasz is not None
    hr = szakasz.find_next_sibling()
    assert hr is not None

    assert hr.name == "hr"

def test_feladat_14_2(html_soup):
    test_feladat_14(html_soup)

# 15. latvanyok szakasz
def test_feladat_15(html_soup):
    assert html_soup.find("div", class_="latvanyok") is not None

def test_feladat_15_2(html_soup):
    test_feladat_15(html_soup)

# 16. Három div latvany osztállyal
def test_feladat_16(html_soup):
    divs = html_soup.select("div.latvanyok > div.latvany")
    assert len(divs) == 3

def test_feladat_16_2(html_soup):
    test_feladat_16(html_soup)

# 17. Minden latvany tartalmaz h3 és kép
def test_feladat_17(html_soup):
    latvanyok = html_soup.find_all("div", class_="latvany")
    assert len(latvanyok) == 3

    for d in latvanyok:
        assert d.find("h3") is not None and d.find("img") is not None
        assert d.find("img").attrs["src"] is not ""

def test_feladat_17_2(html_soup):
    test_feladat_17(html_soup) 

# 18. latvanyok flexbox elrendezés
def test_feladat_18(css_rules):
    styles = get_style_for_selector(css_rules, ".latvanyok")
    assert styles.get("display") == "flex"
    assert styles.get("justify-content") == "space-evenly"

def test_feladat_18_2(css_rules):
    test_feladat_18(css_rules)

# 19. latvany szöveg középre
def test_feladat_19(css_rules):
    styles = get_style_for_selector(css_rules, ".latvany > h3")
    assert styles.get("text-align") == "center"

def test_feladat_19_2(css_rules):
    test_feladat_19(css_rules)

# 20. fejezet3 szín
def test_feladat_20(css_rules):
    styles = get_style_for_selector(css_rules, ".latvany > h3")
    assert styles.get("color") == "#060"

def test_feladat_20_2(css_rules):
    test_feladat_20(css_rules)

# 21. újabb hr latvanyok után
def test_feladat_21(html_soup):
    szakasz = html_soup.find("div", class_="latvanyok")
    hr = szakasz.find_next_sibling("hr")
    assert hr is not None

def test_feladat_21_2(html_soup):
    test_feladat_21(html_soup)

# 22. erdekessegek szakasz
def test_feladat_22(html_soup):
    assert html_soup.find("div", class_="erdekessegek") is not None

def test_feladat_22_2(html_soup):
    test_feladat_22(html_soup)

# 23. h2 és ul benne
def test_feladat_23(html_soup):
    szakasz = html_soup.find("div", class_="erdekessegek")
    assert szakasz.find("h2") is not None and szakasz.find("ul") is not None

def test_feladat_23_2(html_soup):
    test_feladat_23(html_soup)

# 24. 4 listaelem
def test_feladat_24(html_soup):
    lista = html_soup.find("ul")
    assert lista is not None
    items = lista.find_all("li")
    assert len(items) == 4

    lista = html_soup.find("ul")
    assert len(lista.find_all("li")) == 4

def test_feladat_24_2(html_soup):
    test_feladat_24(html_soup)

# 25. Listaelem betűméret és margó
def test_feladat_25(css_rules):
    styles = get_style_for_selector(css_rules, ".erdekessegek li")
    assert styles.get("font-size") == "18px"
    assert styles.get("margin-bottom") == "10px" or styles.get("margin-top") == "10px"

def test_feladat_25_2(css_rules):
    test_feladat_25(css_rules)