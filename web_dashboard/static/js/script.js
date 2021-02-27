let text = 'Hello, This is Gideon.';
function wake() {
    let msg = new SpeechSynthesisUtterance();
    let voices = window.speechSynthesis.getVoices();
    msg.voice = voices[1];
    msg.voiceURI = "native";
    msg.volume = 1;
    msg.rate = 1.9;
    msg.pitch = 1.9;
    msg.text = text;
    msg.lang = 'en-US';
    speechSynthesis.speak(msg);
}
