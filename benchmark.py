import time
import pandas as pd
import matplotlib.pyplot as plt
from transformers import pipeline
import os

os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

# Petit dataset d'évaluation
test_samples = [
    ("It's an amazin product", "POSITIVE"),
    ("Very bad experience", "NEGATIVE"),
    ("I love it!", "POSITIVE"),
    ("Worst experience ever", "NEGATIVE"),
]

# Trois modèles pour comparaison
models = [
    "distilbert-base-uncased-finetuned-sst-2-english",
    "cardiffnlp/twitter-roberta-base-sentiment-latest",
    "siebert/sentiment-roberta-large-english",
]

def evaluate_model(model_name):
    """Évalue un modèle sur latence + justesse simple"""
    classifier = pipeline("sentiment-analysis", model=model_name)
    total_time, correct = 0.0, 0

    for text, true_label in test_samples:
        start = time.time()
        result = classifier(text)
        elapsed = time.time() - start
        total_time += elapsed

        pred_label = result[0]["label"].upper()
        if pred_label == true_label:
            correct += 1

    avg_latency = total_time / len(test_samples)
    accuracy = correct / len(test_samples)
    return avg_latency, accuracy

def run_benchmark():
    results = []

    for model in models:
        latency, accuracy = evaluate_model(model)
        results.append({
            "Modèle": model,
            "Latence (ms)": round(latency * 1000, 2),
            "Accuracy (%)": round(accuracy * 100, 1),
        })

    # Affichage clair sous forme de tableau
    df = pd.DataFrame(results)
    print("\n=== Résultats du Mini-benchmark ===\n")
    print(df.to_string(index=False))

    return df  # retourner le DataFrame pour le graphique

# -----------------------------
# Exécution et graphique
# -----------------------------
if __name__ == "__main__":
    df = run_benchmark()

    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Barres pour Latence
    ax1.bar(df['Modèle'], df['Latence (ms)'], color='skyblue', label='Latence (ms)')
    ax1.set_ylabel('Latence (ms)', color='blue')
    ax1.set_xlabel('Modèle')
    ax1.tick_params(axis='y', labelcolor='blue')
    ax1.set_xticklabels(df['Modèle'], rotation=25, ha='right')

    # Axe secondaire pour Accuracy
    ax2 = ax1.twinx()
    ax2.plot(df['Modèle'], df['Accuracy (%)'], color='red', marker='o', label='Accuracy (%)')
    ax2.set_ylabel('Accuracy (%)', color='red')
    ax2.tick_params(axis='y', labelcolor='red')
    ax2.set_ylim(0, 110)

    plt.title('Comparaison des modèles : Latence vs Accuracy')
    fig.tight_layout()
    fig.legend(loc="upper right", bbox_to_anchor=(0.9,0.9))

    plt.savefig("benchmark_comparison.png", dpi=300)
    plt.show()
