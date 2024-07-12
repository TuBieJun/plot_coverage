import sys
import matplotlib.pyplot as plt


def plot_coverage(d_depth, outfile, title, step=1, figsize=(30,6), ylim=(0, 100)):
    s = 0
    fig,ax = plt.subplots(figsize=figsize)
    x_label_index = []
    x_label_name = []
    for k,v in d_depth.items():
        block = v[::step]
        l = len(block)
        x_label_index.append(int((s+s+l)/2))
        x_label_name.append(k)
        ax.scatter(list(range(s, s+l)), block, marker=".")
        s += l
    ax.set_xticks(x_label_index, x_label_name, fontsize=15)
    ax.tick_params("y", labelsize=15)
    ax.set_xlabel("genome", fontsize = 20)
    ax.set_ylabel("depth", fontsize = 20)
    ax.set_ylim(ylim)
    ax.set_title(title, fontsize = 30)
    fig.savefig(outfile)
    

if  __name__ == "__main__":

    if len(sys.argv) != 5:
        print(f"usage: python {sys.argv[0]} <depth_file> <prefix> max_depth step", file=sys.stderr)
        sys.exit(1)
    d_depth = {}
    depth_file = sys.argv[1] # samtools format:chrom\tpos\tdepth
    prefix = sys.argv[2]
    max_depth = int(sys.argv[3])
    step = int(sys.argv[4])

    with open(depth_file) as F:
        for line in F:
            items = line.strip().split("\t")
            if items[0].startswith("G"):
                continue
            d = float(items[2])
            d_depth.setdefault(items[0], []).append(d)
    
    
    plot_coverage(d_depth, prefix, "%s.png"%(prefix), step=step,  ylim=(0, max_depth))
