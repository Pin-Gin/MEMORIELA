export default function ConceptPage() {
  return (
    <main className="subpage">
      <header className="subpageHeader">
        <a className="wordmark" href="/">MEMORIELA - Project.YURA.</a>
        <nav aria-label="Main navigation">
          <a className="active" href="/concept">Concept</a>
          <a href="/about">About</a>
          <a href="/technology">Technology</a>
          <a href="/gallery">Gallery</a>
        </nav>
      </header>

      <section className="conceptPage">
        <span>CONCEPT</span>
        <h1>なぜ、Project.YURAを始めたのか。</h1>
        <p>
          AIを便利な道具としてではなく、記憶を重ね、関係を育てながら、
          長くそばにいられる存在にしたい。
          そんな思いから、Project.YURAは始まりました。
        </p>
      </section>
    </main>
  );
}
