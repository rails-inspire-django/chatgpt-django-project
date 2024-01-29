// This is the scss entry file
import "../styles/index.scss";

// import Turbo and TurboCableStreamSourceElement
import "@hotwired/turbo-rails";

// Stimulus
import { Application } from "@hotwired/stimulus";
import { definitionsFromContext } from "@hotwired/stimulus-webpack-helpers";
import TextareaAutogrow from 'stimulus-textarea-autogrow';

window.Stimulus = Application.start();
const context = require.context("../controllers", true, /\.js$/);
window.Stimulus.load(definitionsFromContext(context));
window.Stimulus.register('textarea-autogrow', TextareaAutogrow);
