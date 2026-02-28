import pytest
import cssutils
import os
import bs4

def get_html():
    with open("index.html", encoding="utf-8") as f: #HTML fájl beolvasása
        return bs4.BeautifulSoup(f, 'html.parser') #Visszadobás egyben
    
def get_css():
    with open("style.css", encoding="utf-8") as f: #CSS fájl beolvasása
        css = cssutils.parseString(f.read())
        return [x for x in css.cssRules if x.type == x.STYLE_RULE]#Visszadobás egyben

def test_file_structure():
    expected = ["index.html",
                "style.css", 
                "szoveg.txt", 
                "hetfo_csirkecomb.jpg", 
                "kedd_makosteszta.jpg", 
                "szerda_halaszle.jpg", 
                "csutortok_rantotthus.jpg",
                "pentek_borsofozelek.jpg",
                "tanyer.gif"] # Az elvárt fájlstruktúra (tanyer.gif hozzáadva)
    
    files = os.listdir("./") #Helyi fájlok listája
    for f in expected:
        assert f in files, f"A hiányzik a(z) {f} fájl!"

#Fájlok beolvasása/átalakítása
html_soup = get_html() #bs4 html oldal
css_list = get_css() #cssutils lista

def GetPropertyValue(selector: str, propName: str):
    assert any(x for x in css_list if x.selectorText == selector), f"Nincs {selector} osztály!" 
    return next(x for x in css_list if x.selectorText == selector).style.getPropertyValue(propName) 

#Feladatok
def test_feladat_1():
    assert GetPropertyValue("body", "color") == "#006", "Helytelen az oldal betűszíne!"
    assert GetPropertyValue("body", "background-color") == "#EF6", "Helytelen a beállított háttérszín!"

def test_feladat_2():
    assert GetPropertyValue("body", "font-style") == "italic", "Nincs dőlt beállítás az oldalon!"

def test_feladat_3():
    assert GetPropertyValue("body", "width") == "50%", "Helytelen az oldal szélessége!"
    assert GetPropertyValue("body", "margin") == "auto", "Nincs középre igazítva az oldal!" 

def test_feladat_4():
    assert html_soup.find("h1") != None, "Nem létezik egyes szintű fejezetcím!"
    assert html_soup.find("h1").text == "Heti étlap", "Helytelen a cím szövege!"

def test_feladat_5():
    assert html_soup.find(class_="hetek") != None, "Nem létezik hetek osztály az oldalon!"
    assert html_soup.find(class_="hetek").name == "div", "A hetek osztályú elem nem div!"

def test_feladat_6():
    elems = [("a", "Előző hét"),
             ("span", "Aktuális hét"),
             ("a", "Következő hét")]
    target = html_soup.find(class_="hetek")
    assert isinstance(target, bs4.Tag), "Nincs hetek osztályú elem!"
    for tag, text in elems:
        assert target.find(name=tag) != None, f"Nem létezik {tag} típusú elem a .hetek div-ben!"

def test_feladat_7():
    assert GetPropertyValue(".hetek", "display") == "flex", "Nincs flex rendezés a .hetek kiválasztón!"
    assert GetPropertyValue(".hetek", "justify-content") == "space-evenly", "Helytelen a rendezés módja!"

def test_feladat_8():
    assert GetPropertyValue("hr", "background-color") == "red", "Helytelen/hiányzik a háttérszín beállítás!"
    assert GetPropertyValue("hr", "border-color") == "red", "Helytelen/hiányzik a szegélyszín beállítás!"

def test_feladat_9():
    target = html_soup.find("hr")
    assert isinstance(target, bs4.Tag), "Nem található hr elem az oldalon!"
    prev_sibl = target.find_previous_sibling()
    next_sibl = target.find_next_sibling()
    assert prev_sibl.get("class")[0] == "hetek", "Helytelen a hr elem elhelyezése!"
    assert next_sibl.name == "hr", "Hiányzik a második hr elem!"

def test_feladat_10():
    target = html_soup.find(class_="egynap")
    assert isinstance(target, bs4.Tag), "Nincs egynap osztályú elem!"
    children = target.findChild("div")
    assert target.name == "div", "Az egynap osztályú elem nem div típusú!"
    assert children.name == "div", "Nem div az egynap elem első eleme!"
    assert children.find_next_sibling().name == "img", "Nem img az egynap elem második eleme!"

def test_feladat_11():
    target = html_soup.find(class_="egynap")
    assert isinstance(target, bs4.Tag), "Nincs egynap osztályú elem!"
    assert GetPropertyValue(".egynap", "display") == "flex"
    assert GetPropertyValue(".egynap", "justify-content") == "space-between", "Helytelen az elrendezés módja!"

def test_feladat_12():
    assert len(html_soup.find_all(name="div", class_="egynap")) == 5, "Helytelen számú 'egynap' div!"
    haystack = html_soup.find_all(name="div", class_="egynap")
    for div_count in range(5):
        target = haystack[div_count]
        if (div_count == 4):
            assert target.find_next_sibling() == None or target.find_next_sibling().name != "div"
        else:
            assert target.find_next_sibling().name == "hr", "Nincs hr az egynapok között!"

def test_feladat_13():
    assert GetPropertyValue(".egynap img", "width") == "230px", "Nem megfelelő a kép szélessége!"

def test_feladat_14():
    assert GetPropertyValue(".egynap", "margin-left") == "15%", "Rossz bal margó!" 
    assert GetPropertyValue(".egynap", "margin-right") == "15%", "Rossz jobb margó!"

def test_feladat_15():
    menu = ["hetfo_csirkecomb.jpg", "kedd_makosteszta.jpg", "szerda_halaszle.jpg", "csutortok_rantotthus.jpg", "pentek_borsofozelek.jpg"]
    haystack = html_soup.find_all("div", class_="egynap")
    assert len(haystack) == 5
    for i in range(5): # Javítva 6-ról 5-re
        assert haystack[i].find("img")['src'] == menu[i], f"Rossz kép a(z) {i+1}. napnál!"

def test_feladat_16():
    last_egynap = html_soup.find_all("div", class_="egynap")[-1]
    hr1 = last_egynap.find_next_sibling()
    hr2 = hr1.find_next_sibling()
    assert hr1.name == "hr" and hr2.name == "hr", "Hiányzik a két hr a végéről!"

def test_feladat_17():
    arakcsik = html_soup.find("div", class_="arakcsik")
    assert arakcsik is not None, "Nincs arakcsik div!"
    children = arakcsik.find_all(recursive=False)
    assert "tanyer.gif" in children[0]['src']
    assert "arak" in children[1].get("class")
    assert "tanyer.gif" in children[2]['src']

def test_feladat_18():
    assert GetPropertyValue(".arakcsik", "display") == "flex"
    assert GetPropertyValue(".arakcsik", "justify-content") == "space-between"

def test_feladat_19():
    arak_div = html_soup.find("div", class_="arak")
    spans = arak_div.find_all("span")
    elvart = ["Napi ár:", "999 Ft", "Heti ár:", "4.995 Ft", "", "4.500 Ft"]
    for i in range(len(elvart)):
        assert spans[i].text.strip() == elvart[i]

def test_feladat_20():
    assert GetPropertyValue(".arak", "display") == "grid"
    gap = GetPropertyValue(".arak", "gap") or GetPropertyValue(".arak", "grid-gap")
    assert "10px" in gap

def test_feladat_21():
    assert GetPropertyValue(".arak", "font-weight") in ["bold", "700"]
    assert GetPropertyValue(".arak", "font-size") == "24px"

def test_feladat_22():
    assert GetPropertyValue(".arakcsik", "justify-content") == "space-between"

def test_feladat_23():
    # A 4.995 Ft áthúzása
    val = GetPropertyValue(".arak span:nth-of-type(4)", "text-decoration")
    assert "line-through" in val

def test_feladat_24():
    arakcsik = html_soup.find("div", class_="arakcsik")
    assert arakcsik.find_next_sibling().name == "hr"

def test_feladat_25():
    p = html_soup.find_all("p")[-1]
    assert "étlapváltozás" in p.text.lower()
    assert GetPropertyValue("p", "text-align") == "center"