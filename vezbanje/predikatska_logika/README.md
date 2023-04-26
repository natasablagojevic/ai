∀ ∃

1.  Zadatak:
            Svako zadovoljstvo se placa.
            Zadovoljstvo se placa.

            z(x) - x je zaovoljstvo
            p(x) - x se placa

            (∀x) (z(x) => p(x))

            A & B , A => B

            Greska:
            (∀x)(z(x) & p(x))

2.  Zadatak:
            Postoji zadovoljstvo koje se placa.

            z(x) - x je zadovoljstvo
            p(x) - x se placa

            * Odnosi se na specifican slucaj, na samo jednu jedniku
            (∃x) (z(x) & p(x))

            Geska:
            Sve je zadovoljstvo i sve se placa
            (∀x) (z(x) => p(x))

3.  Zadatak:
            Ni jedno zadovoljstvo nije posao.

            (∀x) (z(x) => ~p(x))

            z(x) - zadovoljstvo
            p(x) - posao

            Greska:
            (∀x) (z(x) & ~p(x)) # sve je zadovoljstvo i nista nije posao
            (∀x) (z(x) <=> ~p(x))

4.  Zadatak:
            Sve sto lejti to ima krila i lagano je.
            Sve sto pliva to nema krila.
            Sve sto pliva to ne leti.

            l(x) - x leti
            k(x) - x ima krila
            p(x) - x pliva
            lag(x) - x je lagano

            (∀x) (l(x) => (k(x) and lag(x)))
            (∀x) (p(x) => ~k(x))
            (∀x) (p(x) => ~l(x))

5.  Zadatak:
            Dve nemimoilazne prave se seku ili su paralelne.
            Prave koje se seku leze u istoj ravni.
            Prave koje su paralelne leze u istoj ravni.
            Dve nemimoilazne prave leze u istoj ravni.

            m(x, y) - x i y su nemimoilazne
            s(x, y) - x i y se seku
            p(x, y) - x i y su paralelne
            r(x, y) - x i y u istoj ravni

            (∀x)(∀y) (m(x, y) => (s(x, y) or p(x, y)))
            (∀X)(∀Y) (s(x, y) => r(x, y))
            (∀x)(∀y) (p(x, y) => r(x, y))
            (∀x)(∀y) (m(x, y) => r(x, y))

6.  Zadatak:
            Svaka dva brata imaju zajednickog roditelja.
            Roditelj je stariji od deteta.
            Postoje braca.
            Ni jedna osoba nije starija od druge.

            b(x, y) - x i y su braca
            r(x, y) - x roditelj od y
            s(x, y) - x je stariji od y

            (∀x)(∀y)(∃z) (b(x, y) => (r(z, x) and r(z, y)))
            (∀x)(∀y) (r(x, y) => s(x, y))
            (∃x)(∃y) b(x, y)
            (∀x)(∀y) ~s(x, y)

7.  Zadatak:
            Svako ima rodjaka na moru ili planini.
            Ko ima rodjaka na moru, bio je na moru.
            Ko ima rodjaka na planini, bio je na planini.
            Neko nije bio ni na planini, ni na moru.

            rp(x) - x rodjak na planini
            rm(x) - x rodjak na moru
            m(x) - bio na moru
            p(x) - bio na planini

            (∀x) (rm(x) or rp(x))
            (∀x) (rm(x) => m(x))
            (∀x) (rp(x) => p(x))
            (∃x) (~p(x) and ~m(x))

8.  Zadatak:
            Svako ruca kod kuce ili u restoranu.
            Ko ruca u restoranu i nema novca, taj pere sudove u restoranu.
            Janko nema novca.
            Janko ruca kod kuce ili pere sudove u restoranu.

            * predikatski simboli
            rk(x) - x ruca kod kuce
            rr(x) - x ruca u restoranu
            nm(x) - x ima novca
            ps(x) - x pere sudove

            * funkcijski simboli
            j - janko
            ar(j) = 0

            (∀x) (rk(x) or rk(x))
            (∀x) ((rr(x) and nn(x)) => ps(x))
            nn(j)
            rk(j) | ps(j)

9.  Zadatak:
            Ko rano rani, ceo dan je pospan.
            Ko rano rani, ceo da je pospan ili dve srece grabi.
            Ko dve srece grabi, ceo dan je pospan.

            rr(x) - x rano rani
            p(x) - x je pospan
            ds(x) - x dve srece grabi

            (∀x) (rr(x) => p(x))
            (∀x) (rr(x) => (p(x) or ds(x)))
            (∀x) (ds(s) => p(x))

10. Zadatak:
            Ko se vozi avionom dosta zaradjuje.
            Ko dosta zaradjuje puno radi.
            Janko se vozi avionom.
            Janko ne radi puno

            va(x) - x se vozi avionom
            dz(x) - x dosta zaradjuje
            pr(x) - x puno radi
            j - janko

            (∀x) (va(a) => dz(x))
            (∀x) (dz(x) => pr(x))
            ~va(j)
            ~pr(j)

11. Zadatak:
            Ako postoji cipela koja u svakom trenutku odgovara svakoj nozi,
                onda za svaku nogu postoji cipela koja joj u nekom trenutku odgovara
                i za svaku nogu postoji trenutak takav da postoji cipela
                koja joj u tom trenutku odgovara.

            A => (B and C)

            A - cipela koja u svakom trenutku odgovara nozi
            B - za nogu postoji cipela koja joj u trenutku odgovara
            C - nogu  trenutak takav da cipela
                koja joj u trenutku odgovara

            p(x, y, z) - nogi X odgovara cipela Y u trenutku Z

            (∃y)(∀z)(∀x)p(x, y, z) => ((∀x)(∃y)(∃z)p(x, y, z) and (∀x)(∃z)(∃y)p(x, y, z))

12. Zadatak:
            Ko laze taj krade.
            Ko krade i uhvacen je u kradji, taj ide u zatvor.
            Al Kapone laze.
            Al Kapone je uhvacen u kradji.
            Laki Luciano laze.

            * P:
            l(x) - x laze
            k(x) - x krade
            u(x) - x je uhvacen u kraci
            z(x) - x ide u zatvor

            * F:
            ak - Al Kapone
            ll- Laki Luciano

            (∀x) (l(x) => k(x))
            (∀x) ((k(x) and u(x)) => z(x))
            l(ak)
            u(ak)
            l(ll)

13. Zadatak:
            Ako onaj ko laze taj i krade i ako bar neko laze, onda neko i krade.

            l(x) - x laze
            k(x) - x krade

            ((∀x)l(x) => k(x) and ((∃x)l(x) =>(∃x)k(x)))

14. Zadatak:
            Ako je X prijatelj osobe Y, onda je Y prijatelj osobe X.
            Ako je X prijatelj osobe Y, onda X voli Y.
            Ne postoji neko ko je povredio osobu koju voli.
            Janko je povredio svog prijatelja Marka.

            p(x, y) - x prijatelj y
            v(x, y) - x voli y
            pov(x, y) - x povredio y

            j - janko
            m - marko

            (∀x)(Vy) (p(x, y) => p(y, x))
            (∀x)(∀y) (p(x, y) => v(x, y))
            ~((∃x)(∃y) (pov(x, y) and v(x, y)))
            pov(j, m) and p(m, j)
