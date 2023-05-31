class AppComponent extends HTMLElement {
  static is = "cell-component";
  connectedCallback() {
    this.className = "box";
  }
}
customElements.define(AppComponent.is, AppComponent);
