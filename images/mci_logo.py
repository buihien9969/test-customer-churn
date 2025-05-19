import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
import os

# Create a simple MCI logo
fig, ax = plt.subplots(figsize=(4, 2))
ax.set_xlim(0, 10)
ax.set_ylim(0, 5)
ax.axis('off')

# Add MCI text
ax.text(1, 2.5, "MCI", fontsize=60, fontweight='bold', color='#00418e')

# Add tagline
ax.text(1, 1.5, "TELECOMMUNICATIONS", fontsize=14, color='#0072c6')

# Save the logo
plt.tight_layout()
plt.savefig('images/mci_logo.png', dpi=300, bbox_inches='tight', transparent=True)
plt.close()

print("MCI logo created successfully!")
