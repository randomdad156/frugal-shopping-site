"""Writes the Frugal Shopping public pages (privacy, terms, account deletion; EN + RO)."""
import io
import os

import pathlib
OUT = str(pathlib.Path(__file__).resolve().parent.parent)
EMAIL = 'adrian.vaiesu+frugalshopping@gmail.com'
DEV = 'Adrian Vaiesu'
DATE_EN = '19 October 2026'
DATE_RO = '19 octombrie 2026'

CSS = """:root { --bg:#ffffff; --fg:#18181b; --muted:#52525b; --line:#e4e4e7; --brand:#0e4a56; --link:#0b6e7a; --card:#f4f4f5; }
@media (prefers-color-scheme: dark) { :root { --bg:#09090b; --fg:#f4f4f5; --muted:#a1a1aa; --line:#27272a; --brand:#5fc6cf; --link:#7fd6de; --card:#18181b; } }
* { box-sizing: border-box; }
body { margin:0; background:var(--bg); color:var(--fg); font:16px/1.6 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif; }
main { max-width: 760px; margin: 0 auto; padding: 32px 16px 64px; }
header { display:flex; justify-content:space-between; align-items:center; gap:12px; flex-wrap:wrap; border-bottom:1px solid var(--line); padding-bottom:16px; margin-bottom:24px; }
header a.brand { color:var(--brand); font-weight:700; text-decoration:none; font-size:18px; }
nav a { color:var(--link); margin-left:12px; }
h1 { font-size: 28px; line-height:1.25; margin: 0 0 4px; }
h2 { font-size: 20px; margin: 32px 0 8px; }
p.meta { color: var(--muted); margin-top: 0; }
a { color: var(--link); }
table { width:100%; border-collapse: collapse; margin: 12px 0; font-size: 15px; }
th, td { text-align:left; vertical-align:top; padding: 8px; border-bottom: 1px solid var(--line); }
th { color: var(--muted); font-weight:600; }
.card { background: var(--card); border-radius: 12px; padding: 16px; margin: 16px 0; }
footer { margin-top: 48px; color: var(--muted); font-size: 14px; border-top:1px solid var(--line); padding-top:16px; }
@media (max-width: 600px) { table, thead, tbody, tr, th, td { display:block; } thead { display:none; } td { border:none; padding:2px 0; } tr { border-bottom:1px solid var(--line); padding:8px 0; } }
"""

L = {
    'en': dict(
        lang='en', prefix='', other='ro/', other_label='Română', home='Frugal Shopping',
        privacy='Privacy policy', terms='Terms of use', delete='Delete your account',
        updated=f'Last updated: {DATE_EN}', footer=f'Frugal Shopping · {DEV}, Romania · <a href="mailto:{EMAIL}">{EMAIL}</a>',
    ),
    'ro': dict(
        lang='ro', prefix='ro/', other='../', other_label='English', home='Frugal Shopping',
        privacy='Politica de confidențialitate', terms='Termeni de utilizare', delete='Șterge-ți contul',
        updated=f'Ultima actualizare: {DATE_RO}', footer=f'Frugal Shopping · {DEV}, România · <a href="mailto:{EMAIL}">{EMAIL}</a>',
    ),
}


def page(lang, name, title, body):
    c = L[lang]
    up = '../' if lang == 'ro' else ''
    html = f"""<!doctype html>
<html lang="{c['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · Frugal Shopping</title>
<link rel="stylesheet" href="{up}style.css">
</head>
<body>
<main>
<header>
  <a class="brand" href="index.html">Frugal Shopping</a>
  <nav><a href="privacy.html">{c['privacy']}</a><a href="terms.html">{c['terms']}</a><a href="delete-account.html">{c['delete']}</a><a href="{c['other']}{name}" hreflang="{'ro' if lang == 'en' else 'en'}">{c['other_label']}</a></nav>
</header>
<h1>{title}</h1>
<p class="meta">{c['updated']}</p>
{body}
<footer>{c['footer']}</footer>
</main>
</body>
</html>
"""
    path = os.path.join(OUT, c['prefix'], name)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    io.open(path, 'w', encoding='utf-8', newline='\n').write(html)


PRIVACY_EN = f"""
<p>Frugal Shopping is a shopping-list app that matches your list with current supermarket offers in Romania. It is made by <strong>{DEV}</strong>, an individual developer in Romania, who is the data controller for the data described here. Contact: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<p>In short: we collect only what the app needs to work, we don’t sell your data, there are no ads and no analytics or tracking, and you can delete your account and all its data at any time.</p>

<h2>What we collect, and why</h2>
<table>
<thead><tr><th>Data</th><th>Why</th><th>Kept</th></tr></thead>
<tbody>
<tr><td><strong>Account:</strong> the email address and name from your Google or Apple account, and which of them you sign in with (one Google and one Apple sign-in can be linked to the same account)</td><td>To create your account, sign you in and sync your lists across devices</td><td>Until you delete the account</td></tr>
<tr><td><strong>Your lists:</strong> products, quantities, units, notes, chosen offers and stores, categories you set, favorite store branches, list order, price alerts</td><td>That’s the app: keeping your lists and matching them with offers</td><td>Until you delete them or the account</td></tr>
<tr><td><strong>People you share a list with:</strong> the email address you invite</td><td>To give them access to the list when they sign in with that email. We don’t email them; you send the invitation yourself from your phone.</td><td>Until the list is deleted or they’re removed</td></tr>
<tr><td><strong>Approximate location</strong>, only when you open the Route tab and allow it</td><td>To find the nearest store branches and plan the route. It’s sent to our server and to the routing service (OpenRouteService) to calculate the route.</td><td>Not stored. Used for the request only.</td></tr>
<tr><td><strong>Push notification token</strong>, only if you allow notifications</td><td>To notify you when an item you’re watching goes on offer</td><td>Until you sign out or delete the account</td></tr>
<tr><td><strong>Plan</strong> (Free, Premium, lifetime)</td><td>To unlock Premium features</td><td>Until you delete the account</td></tr>
</tbody>
</table>
<p>We don’t collect your contacts, photos, precise GPS location, background location, advertising ID or browsing history. You sign in with Google or Apple, so we never see or store a password.</p>

<h2>Legal basis (GDPR)</h2>
<p>We process your account and list data to provide the service you asked for (contract, Art. 6(1)(b) GDPR). Location and notifications are used only with your permission (consent, Art. 6(1)(a)), which you can withdraw at any time in Android’s settings.</p>

<h2>Who processes the data for us</h2>
<table>
<thead><tr><th>Service</th><th>What for</th><th>Where</th></tr></thead>
<tbody>
<tr><td>Supabase</td><td>Database, sign-in and server functions</td><td>EU (Frankfurt, Germany)</td></tr>
<tr><td>Google (Sign in with Google, Google Maps)</td><td>Signing in with Google; showing the map. Opening “Directions in Google Maps” sends the route to Google Maps.</td><td>Google’s data centers</td></tr>
<tr><td>Apple (Sign in with Apple, iPhone only)</td><td>Signing in with Apple</td><td>Apple’s data centers</td></tr>
<tr><td>OpenRouteService (HeiGIT gGmbH)</td><td>Calculating driving routes from your approximate location</td><td>Germany</td></tr>
<tr><td>Expo (650 Industries)</td><td>Delivering push notifications and app updates</td><td>USA (Standard Contractual Clauses)</td></tr>
</tbody>
</table>
<p>Supermarket offers shown in the app come from public catalogs and contain no personal data. We don’t sell or rent your data to anyone, and we don’t share it for advertising.</p>

<h2>Security</h2>
<p>All data is sent over encrypted connections (HTTPS). Access to your lists is limited by database rules to you and the people you share them with. Signing in is handled by Google or Apple, including their two-step verification.</p>

<h2>Your rights</h2>
<p>You can ask to access, correct, export or delete your data, or object to its processing, by writing to <a href="mailto:{EMAIL}">{EMAIL}</a>. You can delete your account yourself in the app (Account → Delete account) or as described on <a href="delete-account.html">this page</a>. You can also complain to the Romanian data protection authority, ANSPDCP (<a href="https://www.dataprotection.ro">dataprotection.ro</a>).</p>

<h2>Deleting your data</h2>
<p>Deleting your account removes your account, your lists (including lists you shared with others), price alerts, preferences and push tokens right away. Our hosting provider may keep encrypted backups for a short time before they are overwritten. Lists other people shared with you aren’t deleted; you just leave them.</p>

<h2>Children</h2>
<p>Frugal Shopping is not meant for children under 16, and we don’t knowingly collect data from them.</p>

<h2>Changes</h2>
<p>If this policy changes, we’ll update the date above and, for important changes, tell you in the app.</p>
"""

PRIVACY_RO = f"""
<p>Frugal Shopping este o aplicație de liste de cumpărături care îți potrivește lista cu ofertele curente din supermarketurile din România. Este făcută de <strong>{DEV}</strong>, dezvoltator persoană fizică din România, operatorul datelor descrise aici. Contact: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<p>Pe scurt: colectăm doar ce îi trebuie aplicației ca să funcționeze, nu vindem datele tale, nu avem reclame, analytics sau urmărire, și îți poți șterge oricând contul și toate datele.</p>

<h2>Ce colectăm și de ce</h2>
<table>
<thead><tr><th>Date</th><th>De ce</th><th>Cât le păstrăm</th></tr></thead>
<tbody>
<tr><td><strong>Cont:</strong> adresa de email și numele din contul Google sau Apple și cu care dintre ele te autentifici (la același cont se pot lega o autentificare Google și una Apple)</td><td>Ca să-ți creăm contul, să te autentifici și să-ți sincronizăm listele pe toate dispozitivele</td><td>Până ștergi contul</td></tr>
<tr><td><strong>Listele tale:</strong> produse, cantități, unități, note, ofertele și magazinele alese, categoriile setate, magazinele preferate, ordinea listelor, alertele de preț</td><td>Asta e aplicația: îți păstrează listele și le potrivește cu ofertele</td><td>Până le ștergi pe ele sau contul</td></tr>
<tr><td><strong>Persoanele cu care partajezi o listă:</strong> adresa de email invitată</td><td>Ca să primească acces la listă când se autentifică cu acel email. Noi nu le trimitem emailuri; invitația o trimiți tu de pe telefon.</td><td>Până se șterge lista sau sunt scoși din ea</td></tr>
<tr><td><strong>Locația aproximativă</strong>, doar când deschizi tabul Traseu și permiți</td><td>Ca să găsim cele mai apropiate magazine și să planificăm traseul. E trimisă serverului nostru și serviciului de rutare (OpenRouteService) pentru calcul.</td><td>Nu se stochează. E folosită doar pentru cerere.</td></tr>
<tr><td><strong>Tokenul pentru notificări</strong>, doar dacă permiți notificările</td><td>Ca să te anunțăm când un produs urmărit intră la ofertă</td><td>Până te deconectezi sau ștergi contul</td></tr>
<tr><td><strong>Planul</strong> (Gratuit, Premium, pe viață)</td><td>Ca să deblocăm funcțiile Premium</td><td>Până ștergi contul</td></tr>
</tbody>
</table>
<p>Nu colectăm contactele, pozele, locația GPS precisă, locația în fundal, ID-ul de publicitate sau istoricul de navigare. Te autentifici cu Google sau Apple, așa că nu vedem și nu stocăm nicio parolă.</p>

<h2>Temeiul legal (GDPR)</h2>
<p>Prelucrăm datele contului și ale listelor ca să-ți oferim serviciul cerut (contract, art. 6 alin. (1) lit. b GDPR). Locația și notificările sunt folosite doar cu permisiunea ta (consimțământ, art. 6 alin. (1) lit. a), pe care o poți retrage oricând din setările Android.</p>

<h2>Cine prelucrează datele pentru noi</h2>
<table>
<thead><tr><th>Serviciu</th><th>Pentru ce</th><th>Unde</th></tr></thead>
<tbody>
<tr><td>Supabase</td><td>Baza de date, autentificarea și funcțiile de pe server</td><td>UE (Frankfurt, Germania)</td></tr>
<tr><td>Google (autentificare Google, Google Maps)</td><td>Autentificarea cu Google; afișarea hărții. „Indicații în Google Maps” trimite traseul către Google Maps.</td><td>Centrele de date Google</td></tr>
<tr><td>Apple (autentificare Apple, doar pe iPhone)</td><td>Autentificarea cu Apple</td><td>Centrele de date Apple</td></tr>
<tr><td>OpenRouteService (HeiGIT gGmbH)</td><td>Calculul traseelor auto pornind de la locația aproximativă</td><td>Germania</td></tr>
<tr><td>Expo (650 Industries)</td><td>Livrarea notificărilor și a actualizărilor aplicației</td><td>SUA (Clauze Contractuale Standard)</td></tr>
</tbody>
</table>
<p>Ofertele din aplicație provin din cataloage publice și nu conțin date personale. Nu vindem și nu închiriem datele tale nimănui și nu le folosim pentru publicitate.</p>

<h2>Securitate</h2>
<p>Toate datele circulă prin conexiuni criptate (HTTPS). Accesul la liste e limitat prin regulile bazei de date la tine și la cei cu care le partajezi. Autentificarea e gestionată de Google sau Apple, inclusiv verificarea în doi pași.</p>

<h2>Drepturile tale</h2>
<p>Poți cere acces, rectificarea, exportul sau ștergerea datelor ori te poți opune prelucrării, scriind la <a href="mailto:{EMAIL}">{EMAIL}</a>. Contul îl poți șterge singur din aplicație (Cont → Șterge contul) sau ca pe <a href="delete-account.html">această pagină</a>. Poți depune și o plângere la ANSPDCP (<a href="https://www.dataprotection.ro">dataprotection.ro</a>).</p>

<h2>Ștergerea datelor</h2>
<p>Ștergerea contului elimină imediat contul, listele (inclusiv cele partajate cu alții), alertele, preferințele și tokenurile pentru notificări. Furnizorul de găzduire poate păstra copii de rezervă criptate pentru scurt timp, până sunt suprascrise. Listele partajate de alții cu tine nu se șterg; doar ieși din ele.</p>

<h2>Copii</h2>
<p>Frugal Shopping nu se adresează copiilor sub 16 ani și nu colectăm cu bună știință date de la ei.</p>

<h2>Modificări</h2>
<p>Dacă politica se schimbă, actualizăm data de mai sus și, pentru schimbări importante, te anunțăm în aplicație.</p>
"""

TERMS_EN = f"""
<p>These terms apply to the Frugal Shopping app, made by {DEV} (Romania). By creating an account or using the app you agree to them.</p>
<h2>The service</h2>
<p>Frugal Shopping helps you keep shopping lists and shows current supermarket offers that match them. Offers come from publicly available catalogs and are read automatically, so <strong>prices, dates and products can be wrong or out of date</strong>. Always check the price in the store. Routes and estimated totals are guides, not guarantees.</p>
<h2>Not affiliated with the stores</h2>
<p>Frugal Shopping is an independent app and is not affiliated with, endorsed or sponsored by Lidl, Kaufland, Carrefour, Mega Image, Penny, Auchan, Metro, Selgros or any other retailer. Store names and trademarks belong to their owners and are used only to identify where an offer is available.</p>
<h2>Your account</h2>
<p>You sign in with Google or Apple; keep that account safe, since you are responsible for activity on your Frugal Shopping account. Link only your own Google and Apple accounts. You can delete your account at any time (Account → Delete account, or see <a href="delete-account.html">this page</a>).</p>
<h2>Shared lists and acceptable use</h2>
<p>When you share a list, the people you invite can see and, as editors, change it. Don’t use the app to send unwanted invitations, to harass anyone or for anything illegal. Report abuse to <a href="mailto:{EMAIL}">{EMAIL}</a>; we may suspend accounts that misuse the service.</p>
<h2>Premium</h2>
<p>Some features (such as Optimize, routes, sharing and price alerts) need Premium. When paid plans are available they are sold only through Google Play (or the App Store on iPhone), under their billing terms; subscriptions are managed and cancelled there. Deleting your account doesn’t cancel a store subscription.</p>
<h2>Availability and liability</h2>
<p>The app is provided “as is”. We work to keep it running and accurate but can’t promise it will always be available or error-free. To the extent the law allows, we aren’t liable for indirect losses, such as money spent because of an outdated price. Nothing here limits rights you have as a consumer under Romanian or EU law.</p>
<h2>Changes and law</h2>
<p>We may update these terms; the date above shows the current version, and important changes are announced in the app. Romanian law applies. Questions: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
"""

TERMS_RO = f"""
<p>Acești termeni se aplică aplicației Frugal Shopping, realizată de {DEV} (România). Creând un cont sau folosind aplicația, ești de acord cu ei.</p>
<h2>Serviciul</h2>
<p>Frugal Shopping te ajută să ții liste de cumpărături și îți arată ofertele curente din supermarketuri care se potrivesc cu ele. Ofertele provin din cataloage publice și sunt citite automat, așa că <strong>prețurile, perioadele și produsele pot fi greșite sau depășite</strong>. Verifică mereu prețul în magazin. Traseele și totalurile estimate sunt orientative, nu garanții.</p>
<h2>Nu suntem afiliați magazinelor</h2>
<p>Frugal Shopping este o aplicație independentă și nu este afiliată, susținută sau sponsorizată de Lidl, Kaufland, Carrefour, Mega Image, Penny, Auchan, Metro, Selgros sau alt comerciant. Numele și mărcile magazinelor aparțin proprietarilor lor și sunt folosite doar ca să arate unde e disponibilă o ofertă.</p>
<h2>Contul tău</h2>
<p>Te autentifici cu Google sau Apple; păstrează acel cont în siguranță, pentru că răspunzi de activitatea din contul tău Frugal Shopping. Leagă doar propriile conturi Google și Apple. Îți poți șterge oricând contul (Cont → Șterge contul sau vezi <a href="delete-account.html">această pagină</a>).</p>
<h2>Liste partajate și utilizare acceptabilă</h2>
<p>Când partajezi o listă, cei invitați o pot vedea și, ca editori, modifica. Nu folosi aplicația pentru invitații nedorite, hărțuire sau activități ilegale. Raportează abuzurile la <a href="mailto:{EMAIL}">{EMAIL}</a>; putem suspenda conturile care folosesc abuziv serviciul.</p>
<h2>Premium</h2>
<p>Unele funcții (Optimizare, trasee, partajare, alerte de preț) necesită Premium. Când planurile plătite vor fi disponibile, vor fi vândute doar prin Google Play (sau App Store pe iPhone), conform condițiilor lor de plată; abonamentele se gestionează și se anulează acolo. Ștergerea contului nu anulează abonamentul din magazin.</p>
<h2>Disponibilitate și răspundere</h2>
<p>Aplicația este oferită „ca atare”. Ne străduim să funcționeze și să fie corectă, dar nu putem garanta că va fi mereu disponibilă sau fără erori. În limitele legii, nu răspundem pentru pierderi indirecte, cum ar fi bani cheltuiți din cauza unui preț depășit. Nimic de aici nu îți limitează drepturile de consumator conform legii române sau europene.</p>
<h2>Modificări și legea aplicabilă</h2>
<p>Putem actualiza acești termeni; data de mai sus arată versiunea curentă, iar schimbările importante sunt anunțate în aplicație. Se aplică legea română. Întrebări: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
"""

SUBJ_EN = 'Delete%20my%20Frugal%20Shopping%20account'
SUBJ_RO = 'Sterge%20contul%20Frugal%20Shopping'
DELETE_EN = f"""
<p>You can delete your Frugal Shopping account and all its data at any time, in the app or without it.</p>
<h2>In the app</h2>
<p>Open <strong>Account → Delete account</strong>, read what will be deleted, and confirm. It happens right away.</p>
<h2>Without the app</h2>
<div class="card">
<p>Send an email <strong>from the address you use to sign in</strong> to <a href="mailto:{EMAIL}?subject={SUBJ_EN}">{EMAIL}</a> with the subject “Delete my Frugal Shopping account”.</p>
<p>We’ll confirm by replying to that address and delete the account within 7 days at the latest (usually the same day). If you sign in with Apple using a hidden email, write from the email linked to your Apple ID and mention it.</p>
</div>
<h2>What is deleted</h2>
<ul>
<li>Your account (email, name, linked Google and Apple sign-ins)</li>
<li>Your lists and their products, including lists you shared with others (they lose access too)</li>
<li>Price alerts, favorite stores, remembered categories, list order, push notification tokens, your plan</li>
</ul>
<h2>What is kept</h2>
<p>Nothing linked to you. Our hosting provider may keep encrypted backups for a short time before they are overwritten. Lists other people shared with you stay with their owners. If you bought Premium through Google Play, Google keeps its own purchase records; cancel the subscription in Google Play, since deleting the account doesn’t cancel it.</p>
"""
DELETE_RO = f"""
<p>Îți poți șterge oricând contul Frugal Shopping și toate datele lui, din aplicație sau fără ea.</p>
<h2>Din aplicație</h2>
<p>Deschide <strong>Cont → Șterge contul</strong>, citește ce se șterge și confirmă. Se întâmplă imediat.</p>
<h2>Fără aplicație</h2>
<div class="card">
<p>Trimite un email <strong>de pe adresa cu care te autentifici</strong> la <a href="mailto:{EMAIL}?subject={SUBJ_RO}">{EMAIL}</a> cu subiectul „Șterge contul Frugal Shopping”.</p>
<p>Îți confirmăm răspunzând la acea adresă și ștergem contul în cel mult 7 zile (de obicei în aceeași zi). Dacă te autentifici cu Apple cu email ascuns, scrie de pe emailul asociat Apple ID-ului și menționează asta.</p>
</div>
<h2>Ce se șterge</h2>
<ul>
<li>Contul (email, nume, autentificările Google și Apple legate)</li>
<li>Listele și produsele din ele, inclusiv listele partajate cu alții (și ei pierd accesul)</li>
<li>Alertele de preț, magazinele preferate, categoriile memorate, ordinea listelor, tokenurile pentru notificări, planul</li>
</ul>
<h2>Ce se păstrează</h2>
<p>Nimic legat de tine. Furnizorul de găzduire poate păstra copii de rezervă criptate pentru scurt timp, până sunt suprascrise. Listele partajate de alții cu tine rămân la proprietarii lor. Dacă ai cumpărat Premium prin Google Play, Google își păstrează evidența plăților; anulează abonamentul în Google Play, ștergerea contului nu îl anulează.</p>
"""

INDEX_EN = """
<p>Frugal Shopping: your shopping list, matched with this week’s best supermarket offers in Romania.</p>
<ul>
<li><a href="privacy.html">Privacy policy</a></li>
<li><a href="terms.html">Terms of use</a></li>
<li><a href="delete-account.html">Delete your account</a></li>
</ul>
"""
INDEX_RO = """
<p>Frugal Shopping: lista ta de cumpărături, potrivită cu cele mai bune oferte ale săptămânii din supermarketurile din România.</p>
<ul>
<li><a href="privacy.html">Politica de confidențialitate</a></li>
<li><a href="terms.html">Termeni de utilizare</a></li>
<li><a href="delete-account.html">Șterge-ți contul</a></li>
</ul>
"""

os.makedirs(OUT, exist_ok=True)
io.open(os.path.join(OUT, 'style.css'), 'w', encoding='utf-8', newline='\n').write(CSS)
io.open(os.path.join(OUT, '.nojekyll'), 'w').write('')
page('en', 'index.html', 'Frugal Shopping', INDEX_EN)
page('ro', 'index.html', 'Frugal Shopping', INDEX_RO)
page('en', 'privacy.html', 'Privacy policy', PRIVACY_EN)
page('ro', 'privacy.html', 'Politica de confidențialitate', PRIVACY_RO)
page('en', 'terms.html', 'Terms of use', TERMS_EN)
page('ro', 'terms.html', 'Termeni de utilizare', TERMS_RO)
page('en', 'delete-account.html', 'Delete your Frugal Shopping account', DELETE_EN)
page('ro', 'delete-account.html', 'Șterge-ți contul Frugal Shopping', DELETE_RO)
io.open(os.path.join(OUT, 'README.md'), 'w', encoding='utf-8', newline='\n').write(
    '# Frugal Shopping: public pages\n\nPrivacy policy, terms of use and account deletion for the Frugal Shopping app '
    '(EN and RO), published with GitHub Pages. The app itself lives in a private repository.\n')
print('ok')
