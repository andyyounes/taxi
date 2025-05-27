# taxi
# Mirope - Autonomous Ride Request App

**Mirope** (meaning "one second" in Armenian) is a minimal web interface to request a ride from an autonomous vehicle. It connects to Quanser Virtual Labs (QLabs) and starts the car when the button is pressed.

## 🚗 Features

- One-button ride request interface
- Integrates with Quanser's QLabs API
- Simple and mobile-friendly design
- Deployable using GitHub Pages

## 📂 How to Use

1. Clone or download the repo.
2. Make sure `index.html` is in the root directory.
3. Update the IP and port in the `fetch()` URL inside the HTML to your local or network-accessible Quanser API:

```js
fetch('http://<QUANSER_API_IP>:<PORT>/start', {
