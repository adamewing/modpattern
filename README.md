# modpattern
find modfied base patterns from nanopore data

## Installation

```
git clone https://github.com/adamewing/modpattern.git
cd modpattern
conda env create -f modpattern.yml
conda activate modpattern 
pip install -e $PWD
modpattern -h
```

## Train a model

(details coming soon)

### modpattern train

```

options:
  -h, --help            show this help message and exit
  -b, --bam BAM
  -d, --db DB           methylartist database (unused for .bam file)
  -m, --mod MOD         modificaiton (if not sure, guess and then select from list if error)
  -p, --pos POS         positive examples (BED-3 or folder with images)
  -n, --neg NEG         negative examples (BED-3 or folder with images)
  --min_reads MIN_READS
  --min_motifs MIN_MOTIFS
  --images_only         output images from training input data only (do not train model)
  --tmp TMP
  --procs PROCS
  --testfrac TESTFRAC   fraction of examples used for testing
  --max_epochs MAX_EPOCHS
                        max epochs
```

## Call methylation patterns

### modpattern call

(details coming soon)

```
options:
  -h, --help            show this help message and exit
  -b, --bam BAM
  -f, --fai FAI         reference genome index (.fai from samtools index or list of chrom <tab> length)
  --bed BED             BED=3 file (overrides --fai)
  -d, --db DB           methylartist database(s)
  -m, --mod MOD         modificaiton (if not sure, guess and then select from list if error)
  --model MODEL         trained model
  -p, --peaktype PEAKTYPE
                        methylated (m) or unmethylated (u)
  -w, --width WIDTH     width (should match training data)
  --phased
  -o, --outname OUTNAME
                        output basename (default to random UUID)
  -s, --batchsize BATCHSIZE
                        batch size (default=10000)
  --skip_refine         skip refinement, use for multi-sample comparison
  --min_call_depth MIN_CALL_DEPTH
  --min_peak_width MIN_PEAK_WIDTH
  --min_reads MIN_READS
                        minimum reads to consider a segment (default=10)
  --min_motifs MIN_MOTIFS
                        minimum motifs to consider a segment (default=100)
  --procs PROCS
  --images IMAGES       for debugging
  --debug_dir DEBUG_DIR
                        for debugging
  --tmp TMP
```

## Compare methylation pattern calls

### modpattern compare

(details coming soon)


```
options:
  -h, --help            show this help message and exit
  -d, --data DATA       whitespace-delimited file: .region.bed, .bam, .db, phase (0/1, optional)
  -p, --peaktype PEAKTYPE
                        methylated (m) or unmethylated (u)
  -m, --mod MOD         modificaiton (if not sure, guess and then select from list if error)
  -o, --outname OUTNAME
                        output basename (default to random UUID)
  -w, --search_window SEARCH_WINDOW
  --min_call_depth MIN_CALL_DEPTH
  --min_peak_width MIN_PEAK_WIDTH
  --min_reads MIN_READS
                        minimum reads to consider a segment (default=10)
  --min_motifs MIN_MOTIFS
                        minimum motifs to consider a segment (default=100)
  --procs PROCS
  --tmp TMP

```
