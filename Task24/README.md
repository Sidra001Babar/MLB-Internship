# Caption & Search Photo Gallery

A computer vision project that automatically generates captions for images and allows users to search the image collection using natural-language queries.

The project combines two pretrained vision-language models:

- **BLIP** — generates a natural-language caption for every image.
- **CLIP** — converts images and text into embeddings and finds images that are semantically similar to a user's text query.

The project is designed as a small demonstration pipeline using **20–25 images** and is optimized for CPU-based systems.

---

# 1. Project Objective

The goal of this project is to build a simple AI-powered photo gallery that can:

1. Read images from an input folder.
2. Automatically generate a caption for every image using BLIP.
3. Generate a CLIP embedding for every image.
4. Store the captions and embeddings as an image index.
5. Accept a natural-language search query.
6. Convert the query into a CLIP text embedding.
7. Compare the query embedding against all image embeddings.
8. Return the Top-5 most relevant images.
9. Display each result with:
   - Image name
   - Similarity score
   - BLIP-generated caption
10. Save search results into JSON.
11. Generate visual grids.
12. Test abstract/indirect queries that do not directly name the objects in the images.

---



# 2. Folder Structure

``` text 
Task24/
│
├── app/
│   ├── main.py
│   ├── config.py
│   ├── captioner.py
│   ├── clip_model.py
│   ├── search.py
│   └── visualizer.py
│
├── images/
│   ├── 1.jpg
│   ├── 2.jpg
│   ├── 3.jpg
│   ├── ...
│   └── 20.jpg
│
├── outputs/
│   ├── embeddings/
│   ├── all_images_with_captions.jpg
│   ├── all_search_results.jpg
│   ├── image_index.json
│   ├── search_results.json
│ 
│
└── README.md

```
# 3. How to Run

## 1. Open the Project Folder

Open the terminal inside the `Task24` folder:

```bash
cd Task24
```

## 2. Activate Virtual Environment

**Windows (Command Prompt / PowerShell):**
```bash
venv\Scripts\activate
```

**Linux / macOS:**
```bash
source venv/bin/activate
```

## 3. Run the Application

```bash
python -m app.main
```

## 4. Select an Option

The application will display the following menu:

```text
1. Build / rebuild image index
2. Search images
3. Exit
```

---

### Option 1 — Build / Rebuild Image Index

Select:
```text
Choose an option: 1
```

**This will:**
* Process all images from the `images/` folder.
* Generate a **BLIP** caption for every image.
* Generate a **CLIP** embedding for every image.
* Save the combined image index.
* Generate the all-images caption grid.

**Generated files:**
```text
outputs/
├── embeddings/
├── image_index.json
└── all_images_with_captions.jpg
```

---

### Option 2 — Search Images

Select:
```text
Choose an option: 2
```

Enter a natural-language query:
```text
Enter search query: a red car
```

**Other examples:**
* `someone cooking`
* `travelling`
* `someone is playing`

The system returns the **Top 5** matching images with:
* Rank
* Image name
* CLIP similarity score
* BLIP caption

**Output Files:**
* All searches are stored cumulatively in: `outputs/search_history.json`
* The visual search results grid is stored in: `outputs/all_search_results.jpg`

#### Finish Searching
Type:
```text
exit
```
to stop the search loop.

---

### Option 3 — Exit

Select:
```text
Choose an option: 3
```
to exit the application.

# Conclusion

The Caption & Search Photo Gallery successfully implements an image captioning and natural-language image retrieval pipeline using two pre-trained vision-language models.

BLIP is used to automatically generate captions for all images in the 20–25 image dataset, while CLIP is used to generate image embeddings and match natural-language queries against the stored image embeddings.

The system returns the Top 5 most relevant images for each query along with their similarity scores and BLIP-generated captions. It also preserves multiple search queries and their results in a cumulative JSON history and visual search-results grid.

The project demonstrates that natural-language image search can be performed without manually tagging every image and that the same image dataset can be searched using different types of user queries.