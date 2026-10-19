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
        privacy='Privacy policy', terms='Terms of use', eula='License (EULA)', delete='Delete your account',
        updated=f'Last updated: {DATE_EN}', footer=f'Frugal Shopping · {DEV}, Romania · <a href="mailto:{EMAIL}">{EMAIL}</a>',
    ),
    'ro': dict(
        lang='ro', prefix='ro/', other='../', other_label='English', home='Frugal Shopping',
        privacy='Politica de confidențialitate', terms='Termeni de utilizare', eula='Licență (EULA)', delete='Șterge-ți contul',
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
  <nav><a href="privacy.html">{c['privacy']}</a><a href="terms.html">{c['terms']}</a><a href="eula.html">{c['eula']}</a><a href="delete-account.html">{c['delete']}</a><a href="{c['other']}{name}" hreflang="{'ro' if lang == 'en' else 'en'}">{c['other_label']}</a></nav>
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
<tr><td><strong>Account:</strong> the email address and name from your Google or Apple account, and which of them you sign in with (one Google and one Apple sign-in can be linked to the same account)</td><td>To create your account, sign you in and sync your lists across devices</td><td>Until you delete the account; email and dates then 6 more months in the minimal record (see below)</td></tr>
<tr><td><strong>Your lists:</strong> products, quantities, units, notes, chosen offers and stores, categories you set, favorite store branches, list order, price alerts</td><td>That’s the app: keeping your lists and matching them with offers</td><td>Until you delete them or the account</td></tr>
<tr><td><strong>People you share a list with:</strong> the email address you invite</td><td>To give them access to the list when they sign in with that email. We don’t email them; you send the invitation yourself from your phone. We also note when you sent each invitation (not to whom) to limit spam to 20 a day.</td><td>Until the list is deleted or they’re removed; the times for 2 days</td></tr>
<tr><td><strong>Approximate location</strong>, only when you open the Route tab and allow it</td><td>To find the nearest store branches and plan the route. It’s sent to our server and to the routing service (OpenRouteService) to calculate the route.</td><td>Not stored. Used for the request only.</td></tr>
<tr><td><strong>Push notification token</strong>, only if you allow notifications</td><td>To notify you when an item you’re watching goes on offer</td><td>Until you sign out or delete the account</td></tr>
<tr><td><strong>Plan</strong> (Free, Premium, lifetime)</td><td>To unlock Premium features</td><td>Until you delete the account</td></tr>
<tr><td><strong>Purchases</strong>, only if you buy Premium: which plan, when it started and renews, whether it’s a trial or cancelled, and a purchase identifier from Google Play or the App Store</td><td>To give you Premium and keep it in step with your subscription. Payment details (card, address) stay with Google or Apple; we never see them.</td><td>While you have the account, then 6 months in the minimal record (see below)</td></tr>
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
<tr><td>Google Play, Apple App Store</td><td>Selling Premium and handling payments, under their own privacy policies</td><td>Google’s and Apple’s data centers</td></tr>
<tr><td>RevenueCat</td><td>Checking store purchases and telling us about renewals, cancellations and refunds. It knows your account id and your purchases, not your name or email.</td><td>USA (Standard Contractual Clauses)</td></tr>
<tr><td>Expo (650 Industries)</td><td>Delivering push notifications and app updates</td><td>USA (Standard Contractual Clauses)</td></tr>
</tbody>
</table>
<p>Supermarket offers shown in the app come from public catalogs and contain no personal data. We don’t sell or rent your data to anyone, and we don’t share it for advertising.</p>

<h2>Security</h2>
<p>All data is sent over encrypted connections (HTTPS). Access to your lists is limited by database rules to you and the people you share them with. Signing in is handled by Google or Apple, including their two-step verification.</p>

<h2>Your rights</h2>
<p>Under the GDPR you can access, correct, export or delete your data, restrict or object to its processing, and withdraw consent (for location and notifications) at any time. Most of this is in the app:</p>
<ul>
<li><strong>Get a copy of your data</strong> (access and portability, Art. 15 and 20 GDPR): Account → Download my data. You get a JSON file, a common machine-readable format, with your account, plan, lists, products, alerts and preferences.</li>
<li><strong>Delete your account and data</strong> (Art. 17): Account → Delete account, or as described on <a href="delete-account.html">this page</a>.</li>
<li><strong>Correct</strong> your lists and preferences directly in the app; your name and email come from your Google or Apple account.</li>
</ul>
<p>For anything else, write to <a href="mailto:{EMAIL}">{EMAIL}</a>. We answer within one month (extendable by two months for complex requests, in which case we tell you why). You can also complain to the Romanian data protection authority, ANSPDCP (<a href="https://www.dataprotection.ro">dataprotection.ro</a>).</p>

<h2>Deleting your data, and what we keep for 6 months</h2>
<p>Deleting your account immediately and permanently removes your lists and their products (including lists you shared with others), price alerts, preferences, favorite stores, sign-ins and notification devices. Lists other people shared with you aren’t deleted; you just leave them.</p>
<p>We keep a <strong>minimal record for 6 months</strong>: your account id, email address, sign-up and deletion dates, your plan and purchase history, and which sign-in methods you used. Nothing from your lists. We keep it only to establish, exercise or defend legal claims, such as a payment dispute, a refund or chargeback, or abuse of Premium or account linking (Art. 17(3)(e) and our legitimate interest under Art. 6(1)(f) GDPR). Nobody uses it for anything else, and it’s deleted automatically 6 months after the account was deleted. Our hosting provider may keep encrypted backups for a short time before they are overwritten.</p>
<p>Deleting the account doesn’t cancel a store subscription: cancel it in Google Play or the App Store.</p>

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
<tr><td><strong>Cont:</strong> adresa de email și numele din contul Google sau Apple și cu care dintre ele te autentifici (la același cont se pot lega o autentificare Google și una Apple)</td><td>Ca să-ți creăm contul, să te autentifici și să-ți sincronizăm listele pe toate dispozitivele</td><td>Până ștergi contul; emailul și datele încă 6 luni în evidența minimă (vezi mai jos)</td></tr>
<tr><td><strong>Listele tale:</strong> produse, cantități, unități, note, ofertele și magazinele alese, categoriile setate, magazinele preferate, ordinea listelor, alertele de preț</td><td>Asta e aplicația: îți păstrează listele și le potrivește cu ofertele</td><td>Până le ștergi pe ele sau contul</td></tr>
<tr><td><strong>Persoanele cu care partajezi o listă:</strong> adresa de email invitată</td><td>Ca să primească acces la listă când se autentifică cu acel email. Noi nu le trimitem emailuri; invitația o trimiți tu de pe telefon. Notăm și când ai trimis fiecare invitație (nu cui), ca să limităm spamul la 20 pe zi.</td><td>Până se șterge lista sau sunt scoși din ea; momentele, 2 zile</td></tr>
<tr><td><strong>Locația aproximativă</strong>, doar când deschizi tabul Traseu și permiți</td><td>Ca să găsim cele mai apropiate magazine și să planificăm traseul. E trimisă serverului nostru și serviciului de rutare (OpenRouteService) pentru calcul.</td><td>Nu se stochează. E folosită doar pentru cerere.</td></tr>
<tr><td><strong>Tokenul pentru notificări</strong>, doar dacă permiți notificările</td><td>Ca să te anunțăm când un produs urmărit intră la ofertă</td><td>Până te deconectezi sau ștergi contul</td></tr>
<tr><td><strong>Planul</strong> (Gratuit, Premium, pe viață)</td><td>Ca să deblocăm funcțiile Premium</td><td>Până ștergi contul</td></tr>
<tr><td><strong>Cumpărăturile</strong>, doar dacă cumperi Premium: planul, când a început și când se reînnoiește, dacă e perioadă de probă sau anulat și un identificator al cumpărăturii din Google Play sau App Store</td><td>Ca să-ți dăm Premium și să-l ținem în pas cu abonamentul. Datele de plată (card, adresă) rămân la Google sau Apple; noi nu le vedem.</td><td>Cât ai contul, apoi 6 luni în evidența minimă (vezi mai jos)</td></tr>
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
<tr><td>Google Play, Apple App Store</td><td>Vânzarea Premium și procesarea plăților, conform propriilor politici de confidențialitate</td><td>Centrele de date Google și Apple</td></tr>
<tr><td>RevenueCat</td><td>Verificarea cumpărăturilor din magazin și anunțarea reînnoirilor, anulărilor și rambursărilor. Cunoaște ID-ul contului tău și cumpărăturile, nu numele sau emailul.</td><td>SUA (Clauze Contractuale Standard)</td></tr>
<tr><td>Expo (650 Industries)</td><td>Livrarea notificărilor și a actualizărilor aplicației</td><td>SUA (Clauze Contractuale Standard)</td></tr>
</tbody>
</table>
<p>Ofertele din aplicație provin din cataloage publice și nu conțin date personale. Nu vindem și nu închiriem datele tale nimănui și nu le folosim pentru publicitate.</p>

<h2>Securitate</h2>
<p>Toate datele circulă prin conexiuni criptate (HTTPS). Accesul la liste e limitat prin regulile bazei de date la tine și la cei cu care le partajezi. Autentificarea e gestionată de Google sau Apple, inclusiv verificarea în doi pași.</p>

<h2>Drepturile tale</h2>
<p>Conform GDPR îți poți accesa, rectifica, exporta sau șterge datele, poți restricționa prelucrarea sau te poți opune ei și îți poți retrage oricând consimțământul (pentru locație și notificări). Majoritatea se fac din aplicație:</p>
<ul>
<li><strong>O copie a datelor tale</strong> (acces și portabilitate, art. 15 și 20 GDPR): Cont → Descarcă datele mele. Primești un fișier JSON, un format uzual, citibil automat, cu contul, planul, listele, produsele, alertele și preferințele.</li>
<li><strong>Ștergerea contului și a datelor</strong> (art. 17): Cont → Șterge contul sau ca pe <a href="delete-account.html">această pagină</a>.</li>
<li><strong>Rectificarea</strong> listelor și preferințelor, direct în aplicație; numele și emailul vin din contul Google sau Apple.</li>
</ul>
<p>Pentru orice altceva, scrie la <a href="mailto:{EMAIL}">{EMAIL}</a>. Răspundem în cel mult o lună (prelungibil cu două luni pentru cereri complexe, caz în care îți spunem de ce). Poți depune și o plângere la ANSPDCP (<a href="https://www.dataprotection.ro">dataprotection.ro</a>).</p>

<h2>Ștergerea datelor și ce păstrăm 6 luni</h2>
<p>Ștergerea contului elimină imediat și definitiv listele și produsele din ele (inclusiv listele partajate cu alții), alertele, preferințele, magazinele preferate, autentificările și dispozitivele pentru notificări. Listele partajate de alții cu tine nu se șterg; doar ieși din ele.</p>
<p>Păstrăm o <strong>evidență minimă timp de 6 luni</strong>: ID-ul contului, adresa de email, datele înregistrării și ștergerii, planul și istoricul plăților și metodele de autentificare folosite. Nimic din liste. O păstrăm doar pentru constatarea, exercitarea sau apărarea unor drepturi în instanță, de exemplu o dispută de plată, o rambursare sau contestare a plății ori folosirea abuzivă a Premium sau a legării conturilor (art. 17 alin. (3) lit. e) și interesul nostru legitim, art. 6 alin. (1) lit. f) GDPR). Nu e folosită în alt scop și se șterge automat la 6 luni după ștergerea contului. Furnizorul de găzduire poate păstra copii de rezervă criptate pentru scurt timp, până sunt suprascrise.</p>
<p>Ștergerea contului nu anulează un abonament din magazin: anulează-l în Google Play sau App Store.</p>

<h2>Copii</h2>
<p>Frugal Shopping nu se adresează copiilor sub 16 ani și nu colectăm cu bună știință date de la ei.</p>

<h2>Modificări</h2>
<p>Dacă politica se schimbă, actualizăm data de mai sus și, pentru schimbări importante, te anunțăm în aplicație.</p>
"""

TERMS_EN = f"""
<p>These terms apply to the Frugal Shopping app, made by {DEV} (Romania). By creating an account or using the app you agree to them and to the <a href="eula.html">license agreement (EULA)</a>.</p>
<h2>The service</h2>
<p>Frugal Shopping helps you keep shopping lists and shows current supermarket offers that match them. Offers come from publicly available catalogs and are read automatically, so <strong>prices, dates and products can be wrong or out of date</strong>. Always check the price in the store. Routes and estimated totals are guides, not guarantees.</p>
<h2>Not affiliated with the stores</h2>
<p>Frugal Shopping is an independent app and is not affiliated with, endorsed or sponsored by Lidl, Kaufland, Carrefour, Mega Image, Penny, Auchan, Metro, Selgros or any other retailer. Store names and trademarks belong to their owners and are used only to identify where an offer is available.</p>
<h2>Your account</h2>
<p>You sign in with Google or Apple; keep that account safe, since you are responsible for activity on your Frugal Shopping account. Link only your own Google and Apple accounts. You can delete your account at any time (Account → Delete account, or see <a href="delete-account.html">this page</a>).</p>
<h2>Shared lists and acceptable use</h2>
<p>When you share a list, the people you invite can see and, as editors, change it. Don’t use the app to send unwanted invitations, to harass anyone or for anything illegal. Report abuse to <a href="mailto:{EMAIL}">{EMAIL}</a>; we may suspend accounts that misuse the service.</p>
<h2>Premium</h2>
<p>Some features (such as Optimize, routes, sharing and price alerts) need Premium. Premium is sold only through Google Play (or the App Store on iPhone), under their billing terms, at the price shown in the app before you buy. A monthly subscription renews automatically until you cancel it in the store; new subscribers may get a free first month, and if you cancel at least 24 hours before it ends you aren’t charged. Lifetime is a single payment. Refunds follow the store’s rules. Deleting your account doesn’t cancel a store subscription.</p>
<h2>Availability and liability</h2>
<p>The app is provided “as is”. We work to keep it running and accurate but can’t promise it will always be available or error-free. To the extent the law allows, we aren’t liable for indirect losses, such as money spent because of an outdated price. Nothing here limits rights you have as a consumer under Romanian or EU law.</p>
<h2>Changes and law</h2>
<p>We may update these terms; the date above shows the current version, and important changes are announced in the app. Romanian law applies. Questions: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
"""

TERMS_RO = f"""
<p>Acești termeni se aplică aplicației Frugal Shopping, realizată de {DEV} (România). Creând un cont sau folosind aplicația, ești de acord cu ei și cu <a href="eula.html">acordul de licență (EULA)</a>.</p>
<h2>Serviciul</h2>
<p>Frugal Shopping te ajută să ții liste de cumpărături și îți arată ofertele curente din supermarketuri care se potrivesc cu ele. Ofertele provin din cataloage publice și sunt citite automat, așa că <strong>prețurile, perioadele și produsele pot fi greșite sau depășite</strong>. Verifică mereu prețul în magazin. Traseele și totalurile estimate sunt orientative, nu garanții.</p>
<h2>Nu suntem afiliați magazinelor</h2>
<p>Frugal Shopping este o aplicație independentă și nu este afiliată, susținută sau sponsorizată de Lidl, Kaufland, Carrefour, Mega Image, Penny, Auchan, Metro, Selgros sau alt comerciant. Numele și mărcile magazinelor aparțin proprietarilor lor și sunt folosite doar ca să arate unde e disponibilă o ofertă.</p>
<h2>Contul tău</h2>
<p>Te autentifici cu Google sau Apple; păstrează acel cont în siguranță, pentru că răspunzi de activitatea din contul tău Frugal Shopping. Leagă doar propriile conturi Google și Apple. Îți poți șterge oricând contul (Cont → Șterge contul sau vezi <a href="delete-account.html">această pagină</a>).</p>
<h2>Liste partajate și utilizare acceptabilă</h2>
<p>Când partajezi o listă, cei invitați o pot vedea și, ca editori, modifica. Nu folosi aplicația pentru invitații nedorite, hărțuire sau activități ilegale. Raportează abuzurile la <a href="mailto:{EMAIL}">{EMAIL}</a>; putem suspenda conturile care folosesc abuziv serviciul.</p>
<h2>Premium</h2>
<p>Unele funcții (Optimizare, trasee, partajare, alerte de preț) necesită Premium. Premium se vinde doar prin Google Play (sau App Store pe iPhone), conform condițiilor lor de plată, la prețul afișat în aplicație înainte de cumpărare. Abonamentul lunar se reînnoiește automat până îl anulezi din magazin; abonații noi pot primi prima lună gratuit, iar dacă anulezi cu cel puțin 24 de ore înainte să se termine nu plătești nimic. Varianta pe viață e o singură plată. Rambursările urmează regulile magazinului. Ștergerea contului nu anulează abonamentul din magazin.</p>
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
<h2>What is kept, and for how long</h2>
<p>For <strong>6 months</strong>, only a minimal record for possible legal claims (payment disputes, refunds, abuse): your account id, email, sign-up and deletion dates, plan and purchase history, and sign-in methods. Nothing from your lists. It’s deleted automatically after 6 months. Want a copy of your data first? In the app: Account → Download my data. Our hosting provider may keep encrypted backups for a short time before they are overwritten. Lists other people shared with you stay with their owners. If you bought Premium through Google Play, Google keeps its own purchase records; cancel the subscription in Google Play, since deleting the account doesn’t cancel it.</p>
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
<h2>Ce se păstrează și cât timp</h2>
<p>Timp de <strong>6 luni</strong>, doar o evidență minimă pentru eventuale dispute legale (plăți, rambursări, abuzuri): ID-ul contului, emailul, datele înregistrării și ștergerii, planul și istoricul plăților și metodele de autentificare. Nimic din liste. Se șterge automat după 6 luni. Vrei întâi o copie a datelor? În aplicație: Cont → Descarcă datele mele. Furnizorul de găzduire poate păstra copii de rezervă criptate pentru scurt timp, până sunt suprascrise. Listele partajate de alții cu tine rămân la proprietarii lor. Dacă ai cumpărat Premium prin Google Play, Google își păstrează evidența plăților; anulează abonamentul în Google Play, ștergerea contului nu îl anulează.</p>
"""

EULA_EN = f"""
<p>This End User License Agreement (“EULA”) is between you and {DEV} (Romania), the developer of Frugal Shopping (“the app”). By installing or using the app you accept it. If you don’t, don’t install or use the app. The <a href="terms.html">terms of use</a> and the <a href="privacy.html">privacy policy</a> also apply.</p>
<h2>1. License</h2>
<p>You get a personal, non-exclusive, non-transferable, revocable license to install and use the app on devices you own or control, for your own non-commercial use, under this EULA and the rules of the store you got it from (Google Play or the App Store).</p>
<h2>2. What you may not do</h2>
<p>You may not copy, modify, distribute, sell, rent or sublicense the app; reverse-engineer, decompile or disassemble it except as far as the law expressly allows despite this restriction; remove notices of ownership; use it to break the law or other people’s rights; or try to get around its security, access limits or Premium features, or overload its servers (for example by automated scraping).</p>
<h2>3. Ownership</h2>
<p>The app, its design and its code belong to {DEV} and are licensed, not sold. Store names, logos and catalog content belong to their owners; the app is not affiliated with any retailer. Map data © OpenStreetMap contributors.</p>
<h2>4. Your content</h2>
<p>Your lists and notes stay yours. You let us store and process them only to run the app for you and the people you share them with, as the privacy policy describes.</p>
<h2>5. Premium and purchases</h2>
<p>Premium is bought through Google Play or the App Store under their terms; subscriptions renew until you cancel them there. Your rights as a consumer under EU and Romanian law are not affected.</p>
<h2>6. Updates and availability</h2>
<p>We may update the app, including automatically, to fix problems, add features or meet legal requirements, and may change or stop features. We try to keep it available but can’t guarantee it will always work without interruptions.</p>
<h2>7. Prices and offers</h2>
<p>Offers are read automatically from public catalogs and may be wrong or out of date. Check prices in the store before you buy.</p>
<h2>8. Warranty and liability</h2>
<p>The app is provided “as is”. To the extent the law allows, we disclaim implied warranties and aren’t liable for indirect or consequential losses. Nothing in this EULA limits liability that can’t be limited by law, such as for intent or gross negligence, or your statutory rights as a consumer.</p>
<h2>9. Ending the license</h2>
<p>You can end it at any time by deleting your account and uninstalling the app. It ends automatically if you break this EULA. Sections 3, 8 and 10 survive.</p>
<h2>10. Law and contact</h2>
<p>Romanian law applies, without depriving you of the protection of the mandatory rules of the country where you live. Contact: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<h2>11. App Store (iPhone)</h2>
<p>If you got the app from Apple’s App Store: this EULA is between you and {DEV}, not Apple. Apple has no obligation to provide maintenance or support, and isn’t responsible for the app, any claims about it (including product liability, legal or regulatory compliance, or intellectual property claims) or warranty, except that if the app doesn’t conform to an applicable warranty you may notify Apple, which may refund the purchase price. Apple and its subsidiaries are third-party beneficiaries of this EULA and may enforce it. You confirm you’re not in a country under a U.S. Government embargo and aren’t on a U.S. Government list of prohibited or restricted parties.</p>
"""

EULA_RO = f"""
<p>Acest Acord de licență pentru utilizatorul final („EULA”) este încheiat între tine și {DEV} (România), dezvoltatorul Frugal Shopping („aplicația”). Instalând sau folosind aplicația îl accepți. Dacă nu ești de acord, nu instala și nu folosi aplicația. Se aplică și <a href="terms.html">termenii de utilizare</a> și <a href="privacy.html">politica de confidențialitate</a>.</p>
<h2>1. Licența</h2>
<p>Primești o licență personală, neexclusivă, netransferabilă și revocabilă de a instala și folosi aplicația pe dispozitivele pe care le deții sau le controlezi, pentru uz propriu, necomercial, conform acestui EULA și regulilor magazinului din care ai obținut-o (Google Play sau App Store).</p>
<h2>2. Ce nu ai voie să faci</h2>
<p>Nu ai voie să copiezi, modifici, distribui, vinzi, închiriezi sau sublicențiezi aplicația; să o decompilezi, dezasamblezi sau să faci inginerie inversă, decât în măsura în care legea permite expres acest lucru; să elimini mențiunile de proprietate; să o folosești pentru a încălca legea sau drepturile altora; sau să încerci să-i ocolești securitatea, limitele de acces ori funcțiile Premium sau să-i suprasoliciți serverele (de exemplu prin extragere automată de date).</p>
<h2>3. Proprietate</h2>
<p>Aplicația, designul și codul ei aparțin lui {DEV} și sunt licențiate, nu vândute. Numele magazinelor, siglele și conținutul cataloagelor aparțin proprietarilor lor; aplicația nu este afiliată niciunui comerciant. Date de hartă © contribuitorii OpenStreetMap.</p>
<h2>4. Conținutul tău</h2>
<p>Listele și notele tale rămân ale tale. Ne permiți să le stocăm și să le prelucrăm doar ca să funcționeze aplicația pentru tine și pentru cei cu care le partajezi, așa cum descrie politica de confidențialitate.</p>
<h2>5. Premium și plăți</h2>
<p>Premium se cumpără prin Google Play sau App Store, conform condițiilor lor; abonamentele se reînnoiesc până le anulezi acolo. Drepturile tale de consumator conform legii europene și române nu sunt afectate.</p>
<h2>6. Actualizări și disponibilitate</h2>
<p>Putem actualiza aplicația, inclusiv automat, pentru a repara probleme, a adăuga funcții sau a respecta cerințe legale și putem schimba sau opri funcții. Ne străduim să fie disponibilă, dar nu putem garanta că va funcționa mereu fără întreruperi.</p>
<h2>7. Prețuri și oferte</h2>
<p>Ofertele sunt citite automat din cataloage publice și pot fi greșite sau depășite. Verifică prețurile în magazin înainte să cumperi.</p>
<h2>8. Garanție și răspundere</h2>
<p>Aplicația este oferită „ca atare”. În limitele legii, nu oferim garanții implicite și nu răspundem pentru pierderi indirecte. Nimic din acest EULA nu limitează răspunderea care nu poate fi limitată prin lege, de exemplu pentru intenție sau culpă gravă, și nici drepturile tale legale de consumator.</p>
<h2>9. Încetarea licenței</h2>
<p>O poți încheia oricând ștergându-ți contul și dezinstalând aplicația. Încetează automat dacă încalci acest EULA. Secțiunile 3, 8 și 10 rămân valabile.</p>
<h2>10. Legea aplicabilă și contact</h2>
<p>Se aplică legea română, fără a te priva de protecția regulilor obligatorii din țara în care locuiești. Contact: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<h2>11. App Store (iPhone)</h2>
<p>Dacă ai obținut aplicația din App Store-ul Apple: acest EULA este încheiat între tine și {DEV}, nu cu Apple. Apple nu are obligația de a oferi întreținere sau asistență și nu răspunde pentru aplicație, pentru pretențiile legate de ea (inclusiv răspunderea pentru produs, conformitatea legală sau proprietatea intelectuală) ori pentru garanție, cu excepția faptului că, dacă aplicația nu respectă o garanție aplicabilă, poți anunța Apple, care îți poate rambursa prețul. Apple și filialele sale sunt terți beneficiari ai acestui EULA și îl pot pune în aplicare. Confirmi că nu te afli într-o țară aflată sub embargo al Guvernului SUA și că nu figurezi pe o listă a părților interzise sau restricționate a Guvernului SUA.</p>
"""

INDEX_EN = """
<p>Frugal Shopping: your shopping list, matched with this week’s best supermarket offers in Romania.</p>
<ul>
<li><a href="privacy.html">Privacy policy</a></li>
<li><a href="terms.html">Terms of use</a></li>
<li><a href="eula.html">License agreement (EULA)</a></li>
<li><a href="delete-account.html">Delete your account</a></li>
</ul>
"""
INDEX_RO = """
<p>Frugal Shopping: lista ta de cumpărături, potrivită cu cele mai bune oferte ale săptămânii din supermarketurile din România.</p>
<ul>
<li><a href="privacy.html">Politica de confidențialitate</a></li>
<li><a href="terms.html">Termeni de utilizare</a></li>
<li><a href="eula.html">Acord de licență (EULA)</a></li>
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
page('en', 'eula.html', 'End User License Agreement (EULA)', EULA_EN)
page('ro', 'eula.html', 'Acord de licență pentru utilizatorul final (EULA)', EULA_RO)
page('en', 'delete-account.html', 'Delete your Frugal Shopping account', DELETE_EN)
page('ro', 'delete-account.html', 'Șterge-ți contul Frugal Shopping', DELETE_RO)
io.open(os.path.join(OUT, 'README.md'), 'w', encoding='utf-8', newline='\n').write(
    '# Frugal Shopping: public pages\n\nPrivacy policy, terms of use and account deletion for the Frugal Shopping app '
    '(EN and RO), published with GitHub Pages. The app itself lives in a private repository.\n')
print('ok')
