# Iskolaudvar – HTML + CSS feladatsor

### Minden módosítást a *style.css* fájlban végezz el!
### A Github Classroom-ba a *style.css* és *index.html* fájlokat kell visszatölteni.
### A szövegeket megtalálod a *szoveg.txt* fájlban!

### A feladat elkezdése előtt futtasd le terminálban a
    pip install pytest bs4 cssutils
### parancsot.
### A parancs lefuttatása nélkül nem fog működni a kiértékelés.
### A kiértékelés használata (a feladat mappájába navigálás után):
``` 
pip install pytest, vagy
python -m pip install pytest, vagy
python3 -m pip install pytest
```
---

## 1 pontos feladatok (10 db)

1. Állítsd be az oldal háttérszínét **#F0F0F0**-ra, a szövegszínt pedig **#333333**-ra!
2. Az oldal betűtípusa legyen **Arial**!
3. A teljes oldal margója és belső margója (padding) legyen **0**!
4. Hozz létre egy **.keret** osztályt, amelynek szélessége 90%, és automatikus margóval vízszintesen középre igazított!
5. A **.keret** osztályon belüli HTML elemek között legyen **50px** függőleges tér!
6. Minden második szintű fejezetcím (**h2**) legyen középre igazítva!
7. A **hr** elemek legyenek **3px** magasak, **#CCC** színűek, és ne legyen szegélyük!
8. Az összes kép szélessége legyen pontosan **300px**!
9. A képeknek legyen **10px-es lekerekített sarka**!
10. A lábléc (**footer**) tartalma legyen középre igazítva!

---

## 2 pontos feladatok (15 db)

11. A főcímként szereplő **egyes szintű fejezetcím** szövege legyen: **Iskolaudvar**.
12. A **bemutato** osztályú div tartalmazzon egy **kettes szintű fejezetcímet** *(Szövege: Bemutatkozás)* és egy **bekezdést** *(Szövege: Az iskolaudvarunk kellemes, zöld környezete ideális a szünetek eltöltésére.)*!
13. A **.bemutato** div **bekezdés** szövege legyen dőlt stílusú!
14. A **bemutato** div után jelenjen meg egy **hr** elválasztó elem!
15. Hozz létre egy új div-et `latvanyok` osztállyal!
16. A `latvanyok` **div** három darab **div** elemet tartalmazzon, mindegyik osztálya **latvany** legyen!
17. Minden **latvany** div tartalmazzon egy **hármas szintű fejezetcímet** (Szövegeik: *Virágágyás, Padok, Sportpálya*) és egy **képet** *(A képek bármely sorrendben lehetnek.)*!
18. A **latvany** div-ek legyenek egymás mellett elrendezve **flexbox** segítségével, egyenletesen elosztva!
19. A **latvany** div-ek szövegei legyenek **középre igazítva**!
20. A **latvany** címsorok (**h3**) színe legyen **#060**!
21. A `latvanyok` szakasz után jelenjen meg egy újabb **hr**!
22. Hozz létre egy új **div-et** `erdekessegek` osztállyal!
23. Ebben a szakaszban legyen egy **kettes szintű fejezetcím** *(Szövege: Érdekességek)* és egy **rendezetlen lista**!
    (Szövegük:
    - *A virágágyást a diákok gondozzák*
    - *A padokat újrafestették tavasszal*
    - *Van egy madáretető is az udvaron*
    - *A sportpályát diákversenyekhez használják*)
24. A **rendezetlen lista** tartalmazzon **4 darab listaelemet**!
25. A lista szövegének betűmérete legyen **18px**, a sorok között pedig legyen **10px** függőleges térköz!

---

Minden CSS módosítást a style.css fájlban végezz el!
