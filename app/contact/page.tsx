export default function ContactPage() {
  return (
    <main className="subpage">
      <header className="subpageHeader">
        <a className="wordmark" href="/">MEMORIELA - Project.YURA</a>
        <nav aria-label="Main navigation">
          <a href="/about">About</a>
          <a href="/technology">Technology</a>
          <a href="/gallery">Gallery</a>
          <a className="active" href="/contact">Contact</a>
        </nav>
      </header>

      <section className="subpageHero center">
        <span>CONTACT</span>
        <h1>Contact</h1>
        <p>お問い合わせ</p>
      </section>

      <section className="simplePage">
        <p>お問い合わせ窓口は現在準備中です。</p>
      </section>
    </main>
  );
}
