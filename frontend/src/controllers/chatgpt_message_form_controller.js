import { Controller } from "@hotwired/stimulus";

export default class extends Controller {
  static values = {
    target: String,
  };

  connect() {
    this.focus();
  }

  focus() {
    // autofocus, so it can work after form reset by turbo stream
    const form = this.element;
    const textarea = form.querySelector("textarea");
    if (textarea) {
      textarea.focus();
    }
  }

  autoSubmit(e) {
    if (!(e.key === "Enter" && (e.metaKey || e.ctrlKey))) return;
    const form = e.target.form;
    if (form) form.requestSubmit();
  }

  scroll(event) {
    if (event.target.tagName === "TEXTAREA") {
      const target = document.querySelector(`#${this.targetValue}`);
      target.scrollTop = target.scrollHeight;
    }
  }
}