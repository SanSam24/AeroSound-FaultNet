
#!/usr/bin/env python3
import argparse
import os
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
import librosa

YAMNET_HANDLE = "https://tfhub.dev/google/yamnet/1"

def load_wav_16k(path):
    wav, sr = librosa.load(path, sr=16000, mono=True)
    return wav.astype(np.float32)

def main():
    parser = argparse.ArgumentParser(description="AeroSound-FaultNet inference")
    parser.add_argument("--audio_path", required=True)
    parser.add_argument("--model_path", default="models/yamnet_fault_classifier.h5")
    args = parser.parse_args()

    if not os.path.exists(args.audio_path):
        raise FileNotFoundError(f"Audio file not found: {args.audio_path}")
    if not os.path.exists(args.model_path):
        raise FileNotFoundError(f"Model file not found: {args.model_path}")

    print("Loading classifier...")
    model = tf.keras.models.load_model(args.model_path)

    print("Loading YAMNet...")
    yamnet = hub.load(YAMNET_HANDLE)

    wav = load_wav_16k(args.audio_path)
    scores, embeddings, spectrogram = yamnet(wav)
    emb = tf.reduce_mean(embeddings, axis=0).numpy().astype(np.float32)[None, :]

    probs = model.predict(emb, verbose=0)[0]
    classes = ["healthy", "faulty"]
    idx = int(np.argmax(probs))

    print(f"Prediction: {classes[idx]} (confidence {probs[idx]:.3f})")

if __name__ == "__main__":
    main()
