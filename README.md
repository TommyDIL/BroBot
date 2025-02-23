# BroBot

BroBot est une IA qui permet de rendre un verdict sur une affaire, en se référant au Bro Code.

## Pré-requis

Vous devez disposez d'Ollama installer sur votre ordinateur. Toutes les instructions nécessaires sont trouvable sur le site officiel : [ollama.com](https://ollama.com/).

## Dataset d'entraînement

Le jeu de données utilisé pour entraîner BroBot est synthétique. Il a été généré en se servant d'un LLM existant (mistral:7b-instruct).

Un nouveau dataset peut être généré en utilisant le script Python correspondant :

`[!] Assurez vous d'avoir un fichier dataset.json au même niveau que le script`
```bash
python3 synthetic_data_generator.py
```

Si vous ne voulez pas en recréer un de zéro, vous pouvez utiliser celui existant, trouvable sur Huggin Face : [TommyDIL/Bro-Cases](https://huggingface.co/datasets/TommyDIL/Bro-Cases).

## Entraînement

L'entraînement a été réalisé sur la plateforme [Kaggle](https://www.kaggle.com) et en utilisant le notebook `ai-notebook-v4.ipynb`.

## Conversion en modèle compatible avec Ollama

Pour transformer les transformers obtenus en modèle compatible avec Ollama, le script `convert_model_to_ollama.py` a été utilisé.

`[!] Assurez vous d'avoir un dossier nommé "brodel" au même niveau que le script`
```bash
python3 convert_model_to_ollama.py
```

Ensuite, il faudra executer la commande suivante :

`[!] Le dossier llama.cpp correspond au dépôt Git [llama.cpp](https://github.com/ggml-org/llama.cpp) qui a été cloné.`
```bash
python3 ./llama.cpp/convert_hf_to_gguf.py ./brodel/ --outfile brobot.gguf --outtype q8_0
```

## Création du modèle Ollama

Puis créer le modèle il faut exécuter la commande suivante :

`[!] Si Ollama ne tourne pas, dans un autre terminal, utilisez la commande "ollama serve".`
```bash
ollama create brobot -f ./Modelfile
```

## Utilisation avec Ollama

Pour utiliser le modèle avec Ollama, il suffit de faire la commande suivante :

`[!] Si Ollama ne tourne pas, dans un autre terminal, utilisez la commande "ollama serve".`
```bash
ollama run brobot
```

En manque d'inspiration ? Voilà un exemple d'affaire que vous pouvez essayer :

`My friends and I prepared an event since a long time. But just yesterday, Kevin decided to cancel to go on a date the same day.`
