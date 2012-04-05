# Python Kurs

---
#Ablauf des Kurses

* 25 min Vortrag
* 5 min Fragen
* 60 min Programmieren

Folien unter: [uves.spline.de/python](uves.spline.de/python)

---
# Womit programmieren wir?

* Texteditor
* Gehirn
* python
    * Programmiersprache
    * Skriptsprache
    * dynamisch typisierte Sprache
    * objektorientiere Sprache

---
# Warum python?

* einfach
* große Standardbiblothek
* praktisch
* awesome

---
# Los geht es

---
# Lernen am praktischen Beispiel

Im Terminal:

    !bash
    # python
    Python 3.2.2 (default, Nov 21 2011, 16:50:59)
    [GCC 4.6.2] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

Für mehr Erfolg: Benutzt ipython

---
# Kommentare

    !python
    >>> #(k)ein Kommentar.

---
# Datatypes

    !python
    >>> "aName"     # ein String
    "aName"
    >>> 1           # ne Zahl
    1
    >>> [1, 2, 3]   # und eine Liste
    [1, 2, 3]
    >>> True
    True
    >>> None
    >>>


---
# Variablen benutzen

    !python
    >>> i = 23
    >>> i
    23
    >>

[wikipedia](https://secure.wikimedia.org/wikipedia/de/wiki/Variable_%28Programmierung%29)

---
# Ausgabe

    !python
    >>> print('Hello World!')
    >>>

---
# Eingabe

    !python
    >>> raw_input('Bitte etwas eingaben: ')
    Bitte etwas eingaben: <Benutzer gibt etwas ein>
    'Hello world!'
    >>>

---
# Vereinfachung

    !python
    >>> 23 + 7
    30
    >>> 42 % 5
    2
    >>> True or False
    True
    >>> 'abc' + 'def'
    'abcdef'

---
# Dicts

    !python
    >>> person = {
        'name' : "foo",
        'age' : 42
    }
    >>> person.['age']
    42
    >>> person.['name'] = 'foobar'


---
# Arrays Benutzen

    !python
    >>> list = [1,2,3] # array liste
    [...]
    >>> list[1]
    2
    >>> list[0] = 23
    >>> list
    [23, 2, 3]
    >>> list.append(4)
    >>> list
    [23, 2, 3, 4]

---
# Verlassen wir nun die Shell

---
# Ein  Programm schreiben

1. Editor öffnen
2. Schreiben
3. abspeichern
4. Terminal öffnen
5. mit *cd <ordner>/<ordner>* ins richtige Verzeichnis wechseln
6. starten mit *python <filename starten>*

---
# Was ist eigentlich ein Programm

    !python

    name = raw_input('Hallo Mensch, nenne deinen Namen')
    print ('Dein Name ist: ' + name)

* squentielle (nacheinander) Auflistung von Befehlen
* interagiert mit der Welt (dem Computer) über Ein- und Ausgabe




---
# Kontrollfluss

Immer nur sequentiell abarbeiten ist langweilig.

    !python
    name = raw_input('Wer ist da?')

    if name == 'yves':
        print('Hallo!')
    elif name == 'philipp'
        print('Jo Maaaaaan!')
    else:
        print('Guten Tag!')


[wikipedia](http://en.wikipedia.org/wiki/Conditional_\(programming\))

---
# Wichtig: Codeblöcke!

    !python
    if True:
        if False:
            print('tf')

    else:
        print('tt')

* werden eingerückt
* können geschachtelt werden
* beginnen nach einem Doppelpunkt

---
# Funktionen

Weil wir code wiederverwenden wollen.

    !python
    def word(string):
        return string + ", word!"

Beispiel:

    !python
    >>> word('Python ist toll')
    "Python ist toll, word!"


[wikipedia](http://en.wikipedia.org/wiki/Subroutine)

---
# Schleifen (for)

    !python
    ponies = [ 'brown', 'yellow', 'pink']
    for color in ponies:
        print('Look! A ' + color + 'pony.')

[wikipedia](http://en.wikipedia.org/wiki/Loop_\(computing\)#Loops)

---
# Schleifen (while)

    !python
    problem='yes'
    while problem != 'no':
        problem = raw_input('Got a problem?')

[wikipedia](http://en.wikipedia.org/wiki/Loop_\(computing\)#Loops)

---
# Endlich Module

    !python
    >>> import time
    >>> time.ctime()
    'Wed Apr  4 16:47:11 2012'

---
# Module

Erstellen:

    !python
    # Inhalt von myTime.py
    def getTime():
        return 'Gleich'

Benutzung:

    !python
    >>> import myTime
    >>> myTime.getTime()
    'Gleich'

---
# Noch Fragen?

---
# Aufgaben und Beispiele? Gibt!

Der einfachste Weg: Auschecken mit git (im Terminal)

    > git clone git://github.com/slomo/python-for-erstis.git
    Cloning into python-for-erstis...
    [...]
    Resolving deltas: 100% (1/1), done.
    > cd python-for-erstis
    > ls
    examples  README.md  slides.md  tasks

Oder ihr ladet sie als zip aus dem [github webinterface](https://github.com/slomo/python-for-erstis/zipball/master).


[mehr zur Benutzung von git](https://freiquell.wordpress.com/2010/02/01/git-fur-anfanger-wie-mich)
oder [für Fans von svn und cvs](https://www.youtube.com/watch?v=4XpnKHJAok8)

---
# mehr Lernmaterial

* [learn python the hardway (Onlinebuch)](http://learnpythonthehardway.org/)
* [umfassendes Onlinebuch von Galileo Press)](http://openbook.galileocomputing.de/python/index.htm)
* [coding bat (Codingchallange)](http://codingbat.com/)

---

#Zusätliche Hilfsmittel

---
# Shell in schnell

Ordner wechseln ( benutzt Tab)

    > cd ordner/unterordner

Wo bin ich?

    > pwd
    /tmp/python-for-erstis
    > cd ..
    > pwd
    /tmp/
    > cd ~
    > pwd
    /home/yves

Absolute Pfade vs. relative Pfade

    > pwd /home/yves/dir/dir2
    > cd /home/yves/.cache  # mit absoluten Pfad
    > cd ../../.cache       # mit relativem Pfad

Inhalt des aktuellen Ordners anzeiegen

    > ls        # welche Dateien und Ordner gibt es?
    > ls -l     # für mehr Infos (Rechte/Benutzer)

---
# Shell in schnell

Programm ausführen

    > ipython               # Programme aus /bin und /usr/bin
    > /opt/usr/bin/python   # mit vollem Pfad
    > ./myProgramm.py       # aus lokalen Verzeichnis

Pythonprogramm ausführbar machen

    > chmod +x programm.py  # nicht das #! /usr/bin/python vergessen
    > ./programm.py

Datei anzeigen

    > cat README.md
    Python for erstis
    =================
    [...]


---
# Objekt Orientierung in Python

    !python
    class Basis:

        def toggleMetho(self): # alle Methode erhalten self als erstes
            self.y = self.y.upper()

    class Extended(Basis): # Vererbung

        def __init__(self,arg ): # Constructor
            self.y = arg

        def appendMethod(self, arg):
            self.y += arg

    ex = Extended("test") # erzeugt neues Objekt
    print(ex.y) # Ausgabe: test
    ex.toggleMethod()
    print(ex.y) # Ausgabe: TEST
    ex.appendMetho('test')
    print(ex.y) # Ausgabe: TESTtest


---
# Mehr über Python

## Ecosystem (Paketverwaltung)

* [Python Package Index](http://pypi.python.org)
* [Packet Installer](http://www.pip-installer.org/en/latest/index.html)
* [Introduction to the python ecosystem](http://mirnazim.org/writings/python-ecosystem-introduction/)

## Interresante Blogeiträge

* [Guide to Python magic methods](http://openbook.galileocomputing.de/python/index.htm)
* [Code Like a Pythonista: Idiomatic Python](http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html)

## Misc

* [webservices ausrollen auf AppEngine](https://developers.google.com/appengine/docs/whatisgoogleappengine)
* [python webframe work](http://flask.pocoo.org/)
