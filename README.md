# Detyra3-Siguria-e-te-dhenave-Grupi18

Detyra e trete ne kuader te lendes "Siguria e te dhenave" ne Fakultetin e Inxhinierise Elektrike dhe Kompjuterike - FIEK.

Aplikacioni ofron një mënyrë për të enkriptuar dhe dekriptuar përmbajtjen e file-ve duke përdorur algoritmin 3DES (Triple Data Encryption Standard) me dy çelësa të gjeneruara rastësisht. Këtu është si operon aplikacioni në disa hapa:
Hapi 1: Ngarkimi i file-it
    Përdoruesi fillon aplikacionin dhe zgjedh opcionin për të enkriptuar ose dekriptuar një file.
    Nëse zgjidh opsionin për të enkriptuar/dekriptuar një file tekst/Markdown (".txt/.md"), aplikacioni hap një dritare të re për të zgjedhur file-in relevante.
    Pasi zgjidhet file-i, përmbajtja e tij ngarkohet në aplikacion për të vazhduar me veprimet e mëtejshme.
    
Hapi 2: Enkriptimi dhe Dekriptimi i Përmbajtjes
    Pas ngarkimit të file-it, përdoruesi klikon butonin për të filluar procesin e enkriptimit dhe dekriptimit.
    Aplikacioni përdor algoritmin 3DES për të kriptuar përmbajtjen e file-it të zgjedhur, duke përdorur dy çelësa të gjeneruara rastësisht dhe një vektor inicializimi (IV).
    Pas enkriptimit, përmbajtja e file-it të enkriptuar shfaqet në një dritare të veçantë.
    Pastaj, aplikacioni dekripton përmbajtjen e enkriptuar përsëri duke përdorur të njëjtat çelësa dhe IV. Përmbajtja e dekriptuar shfaqet në një dritare të veçantë.
    
Hapi 3: Ruajtja e File-it të Enkriptuar
    Nëse përdoruesi zgjedh të enkriptoje një file tekst/Markdown, aplikacioni krijon një file të ri me të njëjtin emër dhe shtojcën "_encrypted" në të njëjtën direktori ku gjendet file-i origjinal.
    File-i i ri i enkriptuar përmban përmbajtjen e enkriptuar të file-it origjinal në një format heksadecimal.
    Aplikacioni tregon një mesazh të suksesit për të konfirmuar që enkriptimi është kryer me sukses dhe specifikon rrugën ku është ruajtur file-i i enkriptuar.

Hapi 4: Ruajtja e File-it të Dekriptuar (vetëm për "otherfiles.py")
    Nëse përdoruesi zgjedh të enkriptoje një file tjetër (jo tekst/Markdown), pasi të jetë kryer enkriptimi, aplikacioni krijon një file të ri me të njëjtën emër dhe shtojcën "_decrypted" në të njëjtën direktori si file-i origjinal.
    File-i i ri të dekriptuar përmban përmbajtjen e file-it origjinal pas dekriptimit.
    Aplikacioni tregon një mesazh të suksesit për të konfirmuar që dekriptimi është kryer me sukses dhe specifikon rrugën ku është ruajtur file-i i dekriptuar.


Grupi 18:Ermal Limaj,
Erza Bërbatovci,
Erza Merovci,
Esra Qerimi.


Pamjet e aplikacionit:
![PHOTO1](/images/Screenshot1.png)

Ne rast se zgjedhim "yes":
![PHOTO2](/images/Screenshot2.png)

Ne rast se zgjedhim "no":
![PHOTO1](/images/Screenshot3.png)


![PHOTO3](/images/Screenshot3.png)

![PHOTO4](/images/Screenshot4.png)
Group 18: Ermal Limaj,
Erza Bërbatovci,
Erza Merovci,
Esra Qerimi.
