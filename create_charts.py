import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap
import os

# Create images directory if it doesn't exist
os.makedirs('images', exist_ok=True)

# Set style for plots
plt.style.use('ggplot')
sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 12
plt.rcParams['font.family'] = 'sans-serif'

# Define MCI colors
MCI_BLUE = '#0072c6'
MCI_DARK_BLUE = '#00418e'
MCI_LIGHT_BLUE = '#87cefa'

# Load data
try:
    train_data = pd.read_csv('Copy of churn-bigml-80.csv')
    test_data = pd.read_csv('Copy of churn-bigml-20.csv')
    
    # Combine data for visualization
    all_data = pd.concat([train_data, test_data], axis=0)
    
    # Convert boolean to int for easier processing
    all_data['Churn'] = all_data['Churn'].map({False: 0, True: 1})
    
    # Print basic info
    print(f"Total records: {len(all_data)}")
    print(f"Churn rate: {all_data['Churn'].mean() * 100:.2f}%")
    
    # 1. Pie Chart - Churn Distribution
    plt.figure(figsize=(8, 8))
    churn_counts = all_data['Churn'].value_counts()
    labels = ['Retained', 'Churned']
    sizes = [churn_counts[0], churn_counts[1]]
    colors = [MCI_LIGHT_BLUE, MCI_BLUE]
    explode = (0, 0.1)  # explode the 2nd slice (Churned)
    
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=90)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    plt.title('Customer Churn Distribution', fontsize=16, fontweight='bold', color=MCI_DARK_BLUE)
    plt.tight_layout()
    plt.savefig('images/pie_churn_distribution.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 2. Line Chart - Profit Increase vs Churn Reduction
    plt.figure(figsize=(10, 6))
    churn_reduction = np.arange(0, 11, 1)  # 0% to 10% reduction
    profit_increase_min = churn_reduction * 5  # 5% profit increase per 1% churn reduction
    profit_increase_max = churn_reduction * 9.5  # 9.5% profit increase per 1% churn reduction
    
    plt.plot(churn_reduction, profit_increase_min, 'o-', color=MCI_BLUE, linewidth=2, label='Conservative Estimate')
    plt.plot(churn_reduction, profit_increase_max, 'o-', color=MCI_DARK_BLUE, linewidth=2, label='Optimistic Estimate')
    plt.fill_between(churn_reduction, profit_increase_min, profit_increase_max, color=MCI_LIGHT_BLUE, alpha=0.3)
    
    plt.xlabel('Churn Rate Reduction (%)', fontsize=14)
    plt.ylabel('Profit Increase (%)', fontsize=14)
    plt.title('Projected Profit Increase vs Churn Reduction', fontsize=16, fontweight='bold', color=MCI_DARK_BLUE)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.tight_layout()
    plt.savefig('images/line_profit_vs_churn.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 3. Bar Chart - Usage Comparison
    plt.figure(figsize=(12, 7))
    
    # Calculate mean usage by churn status
    usage_metrics = ['Total day minutes', 'Total eve minutes', 'Total night minutes', 'Total intl minutes']
    churned = all_data[all_data['Churn'] == 1][usage_metrics].mean()
    retained = all_data[all_data['Churn'] == 0][usage_metrics].mean()
    
    # Prepare data for plotting
    x = np.arange(len(usage_metrics))
    width = 0.35
    
    fig, ax = plt.subplots(figsize=(12, 7))
    rects1 = ax.bar(x - width/2, retained, width, label='Retained Customers', color=MCI_LIGHT_BLUE)
    rects2 = ax.bar(x + width/2, churned, width, label='Churned Customers', color=MCI_BLUE)
    
    # Add labels and title
    ax.set_ylabel('Average Minutes', fontsize=14)
    ax.set_title('Usage Comparison: Churned vs Retained Customers', fontsize=16, fontweight='bold', color=MCI_DARK_BLUE)
    ax.set_xticks(x)
    ax.set_xticklabels([label.replace('Total ', '').replace(' minutes', '') for label in usage_metrics], fontsize=12)
    ax.legend()
    
    # Add value labels on bars
    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            ax.annotate(f'{height:.1f}',
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')
    
    autolabel(rects1)
    autolabel(rects2)
    
    plt.tight_layout()
    plt.savefig('images/bar_usage_comparison.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 4. Bar Chart - Plan Comparison
    plt.figure(figsize=(10, 6))
    
    # Calculate churn rate by plan
    intl_plan_churn = all_data.groupby('International plan')['Churn'].mean() * 100
    vm_plan_churn = all_data.groupby('Voice mail plan')['Churn'].mean() * 100
    
    # Create a DataFrame for easier plotting
    plan_data = pd.DataFrame({
        'International Plan': ['No', 'Yes'],
        'Churn Rate': intl_plan_churn.values
    })
    
    vm_data = pd.DataFrame({
        'Voice Mail Plan': ['No', 'Yes'],
        'Churn Rate': vm_plan_churn.values
    })
    
    # Create subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    
    # Plot International Plan
    sns.barplot(x='International Plan', y='Churn Rate', data=plan_data, ax=ax1, palette=[MCI_LIGHT_BLUE, MCI_BLUE])
    ax1.set_title('Churn Rate by International Plan', fontsize=14, fontweight='bold', color=MCI_DARK_BLUE)
    ax1.set_ylabel('Churn Rate (%)', fontsize=12)
    ax1.set_ylim(0, 50)
    
    # Add value labels
    for i, v in enumerate(plan_data['Churn Rate']):
        ax1.text(i, v + 1, f'{v:.2f}%', ha='center', fontsize=10)
    
    # Plot Voice Mail Plan
    sns.barplot(x='Voice Mail Plan', y='Churn Rate', data=vm_data, ax=ax2, palette=[MCI_LIGHT_BLUE, MCI_BLUE])
    ax2.set_title('Churn Rate by Voice Mail Plan', fontsize=14, fontweight='bold', color=MCI_DARK_BLUE)
    ax2.set_ylabel('Churn Rate (%)', fontsize=12)
    ax2.set_ylim(0, 50)
    
    # Add value labels
    for i, v in enumerate(vm_data['Churn Rate']):
        ax2.text(i, v + 1, f'{v:.2f}%', ha='center', fontsize=10)
    
    plt.tight_layout()
    plt.savefig('images/bar_plan_comparison.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 5. US Map - Churn by State
    plt.figure(figsize=(14, 8))
    
    # Calculate churn rate by state
    state_churn = all_data.groupby('State')['Churn'].mean() * 100
    state_churn = state_churn.reset_index()
    state_churn.columns = ['State', 'Churn Rate']
    
    # Sort by churn rate
    state_churn = state_churn.sort_values('Churn Rate', ascending=False)
    
    # Create a horizontal bar chart
    plt.figure(figsize=(12, 10))
    bars = plt.barh(state_churn['State'], state_churn['Churn Rate'], color=MCI_BLUE)
    
    # Highlight states with highest and lowest churn
    colors = [MCI_DARK_BLUE if x > 25 else MCI_LIGHT_BLUE if x < 7 else MCI_BLUE for x in state_churn['Churn Rate']]
    for bar, color in zip(bars, colors):
        bar.set_color(color)
    
    plt.xlabel('Churn Rate (%)', fontsize=14)
    plt.ylabel('State', fontsize=14)
    plt.title('Churn Rate by State', fontsize=16, fontweight='bold', color=MCI_DARK_BLUE)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig('images/map_state_churn.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 6. Feature Importance Chart
    # Create sample feature importance data
    features = ['International Plan', 'Customer Service Calls', 'Total Intl Calls', 
                'Number Vmail Messages', 'Total Day Minutes', 'Total Eve Minutes',
                'Total Intl Minutes', 'State_DC', 'Total Eve Charge', 'Total Night Minutes']
    
    importance = [17.37, 9.40, 7.94, 7.59, 7.47, 4.19, 3.76, 3.37, 2.95, 2.79]
    
    # Create DataFrame
    feature_imp = pd.DataFrame({
        'Feature': features,
        'Importance': importance
    })
    
    # Sort by importance
    feature_imp = feature_imp.sort_values('Importance', ascending=True)
    
    # Plot
    plt.figure(figsize=(10, 8))
    bars = plt.barh(feature_imp['Feature'], feature_imp['Importance'], color=MCI_BLUE)
    
    # Highlight top 3 features
    for i, bar in enumerate(bars):
        if i >= len(bars) - 3:  # Top 3 features
            bar.set_color(MCI_DARK_BLUE)
    
    plt.xlabel('Importance (%)', fontsize=14)
    plt.title('Feature Importance in XGBoost Model', fontsize=16, fontweight='bold', color=MCI_DARK_BLUE)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig('images/bar_feature_importance.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 7. Confusion Matrix
    # Create a sample confusion matrix
    cm = np.array([[566, 4], [26, 71]])
    
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False,
                xticklabels=['Predicted No Churn', 'Predicted Churn'],
                yticklabels=['Actual No Churn', 'Actual Churn'])
    
    plt.title('Confusion Matrix for XGBoost Model', fontsize=16, fontweight='bold', color=MCI_DARK_BLUE)
    plt.tight_layout()
    plt.savefig('images/confusion_matrix.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 8. Implementation Timeline
    plt.figure(figsize=(12, 6))
    
    # Create timeline data
    phases = ['Short-term', 'Medium-term', 'Long-term']
    durations = [3, 3, 6]  # months
    starts = [0, 3, 6]  # start month
    
    # Create horizontal bar chart for timeline
    plt.barh(phases, durations, left=starts, color=[MCI_LIGHT_BLUE, MCI_BLUE, MCI_DARK_BLUE])
    
    # Add milestone markers
    milestones = [
        (1, 'Service Improvement'),
        (2, 'Plan Redesign'),
        (4, 'New Pricing'),
        (5, 'Warning System'),
        (7, 'Loyalty Program'),
        (10, 'Feedback Loop')
    ]
    
    for month, label in milestones:
        plt.scatter(month, 0.5, s=100, color='white', edgecolor='black', zorder=5)
        plt.text(month, 0.3, label, ha='center', va='top', rotation=90, fontsize=10)
    
    plt.xlabel('Months', fontsize=14)
    plt.title('Implementation Timeline', fontsize=16, fontweight='bold', color=MCI_DARK_BLUE)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.xlim(0, 12)
    plt.tight_layout()
    plt.savefig('images/timeline.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 9. Impact vs Difficulty Matrix
    plt.figure(figsize=(10, 8))
    
    # Create a scatter plot for the matrix
    actions = [
        ('Review Int\'l Plan', 0.9, 0.4),
        ('Usage Alerts', 0.7, 0.3),
        ('Tiered Plans', 0.8, 0.6),
        ('Proactive Outreach', 0.8, 0.5),
        ('Service Training', 0.6, 0.4),
        ('VIP Team', 0.7, 0.7),
        ('Unlimited Plans', 0.6, 0.5),
        ('Loyalty Discounts', 0.5, 0.3),
        ('Regional Campaigns', 0.7, 0.8)
    ]
    
    x = [difficulty for _, _, difficulty in actions]
    y = [impact for _, impact, _ in actions]
    labels = [name for name, _, _ in actions]
    
    plt.figure(figsize=(10, 8))
    plt.scatter(x, y, s=200, color=MCI_BLUE, alpha=0.7)
    
    # Add labels to each point
    for i, label in enumerate(labels):
        plt.annotate(label, (x[i], y[i]), xytext=(5, 5), textcoords='offset points')
    
    # Add quadrant lines and labels
    plt.axvline(x=0.5, color='gray', linestyle='--', alpha=0.5)
    plt.axhline(y=0.5, color='gray', linestyle='--', alpha=0.5)
    
    plt.text(0.25, 0.75, 'QUICK WINS', fontsize=12, ha='center', va='center', alpha=0.7)
    plt.text(0.75, 0.75, 'MAJOR PROJECTS', fontsize=12, ha='center', va='center', alpha=0.7)
    plt.text(0.25, 0.25, 'FILL-INS', fontsize=12, ha='center', va='center', alpha=0.7)
    plt.text(0.75, 0.25, 'THANKLESS TASKS', fontsize=12, ha='center', va='center', alpha=0.7)
    
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.xlabel('Implementation Difficulty', fontsize=14)
    plt.ylabel('Impact on Churn Reduction', fontsize=14)
    plt.title('Impact vs. Implementation Difficulty Matrix', fontsize=16, fontweight='bold', color=MCI_DARK_BLUE)
    plt.tight_layout()
    plt.savefig('images/impact_matrix.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print("All charts created successfully!")
    
except Exception as e:
    print(f"Error creating charts: {e}")
