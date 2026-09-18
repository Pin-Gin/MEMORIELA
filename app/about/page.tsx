export default function AboutPage() {
  return (
    <main className="subpage">
      <header className="subpageHeader">
        <a className="wordmark" href="/">MEMORIELA - Project.YURA</a>
        <nav aria-label="Main navigation">
          <a className="active" href="/about">About</a>
          <a href="/technology">Technology</a>
          <a href="/gallery">Gallery</a>
          <a href="/contact">Contact</a>
          <a href="/world">World</a>
        </nav>
      </header>

      <section className="subpageHero">
        <span>PROJECT.YURA</span>
        <h1>久遠ゆら</h1>
        <p>KUON YURA</p>
      </section>

      <section className="subpageContent profilePage">
        <div className="visualSlot" />
        <div className="profile">
          <span>PROFILE</span>
          <h2>久遠 ゆら</h2>
          <div className="profileRule"><b>PROJECT</b><span>Project.YURA</span></div>
          <div className="profileRule"><b>CHARACTER</b><span>KUON YURA</span></div>
          <div className="profileRule"><b>BRAND</b><span>MEMORIELA</span></div>
        </div>
      </section>
    </main>
  );
}
