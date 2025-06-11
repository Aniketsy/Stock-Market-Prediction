import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.express as px


# Set a consistent style
sns.set(style="whitegrid", palette="Set2", font_scale=1.2)

# Sample data
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [200, 250, 300, 400],
    'Category': ['A', 'B', 'C', 'D'],
    'Profit': [20, 30, 25, 35]
}
df = pd.DataFrame(data)

# Line Chart: Sales over Months (trend)
plt.figure(figsize=(7, 4))
plt.plot(df['Month'], df['Sales'], marker='o', color='#2a9d8f', linewidth=2)
plt.title('Sales Trend Over Months', fontsize=16)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Sales', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
for i, value in enumerate(df['Sales']):
    plt.text(df['Month'][i], value+5, str(value), ha='center', fontsize=10)
plt.tight_layout()
plt.show()

# Bar Chart: Sales by Category (comparison)
plt.figure(figsize=(7, 4))
bar = sns.barplot(x='Category', y='Sales', data=df, palette='Set2')
plt.title('Sales by Category', fontsize=16)
plt.xlabel('Category', fontsize=12)
plt.ylabel('Sales', fontsize=12)
for p in bar.patches:
    bar.annotate(format(p.get_height(), '.0f'),
                 (p.get_x() + p.get_width() / 2., p.get_height()),
                 ha = 'center', va = 'center', fontsize=10, color='black', xytext=(0, 8),
                 textcoords = 'offset points')
plt.tight_layout()
plt.show()

# Pie Chart: Proportion of Sales by Category
plt.figure(figsize=(6, 6))
colors = sns.color_palette('Set2')
plt.pie(df['Sales'], labels=df['Category'], autopct='%1.1f%%', startangle=90, colors=colors, textprops={'fontsize': 12})
plt.title('Sales Proportion by Category', fontsize=16)
plt.tight_layout()
plt.show()

# Scatter Plot: Sales vs. Profit (relationship)
plt.figure(figsize=(7, 4))
sns.scatterplot(x='Sales', y='Profit', data=df, s=100, color='#e76f51', edgecolor='black')
plt.title('Sales vs. Profit', fontsize=16)
plt.xlabel('Sales', fontsize=12)
plt.ylabel('Profit', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
for i in range(len(df)):
    plt.text(df['Sales'][i]+2, df['Profit'][i], f"({df['Sales'][i]}, {df['Profit'][i]})", fontsize=10)
plt.tight_layout()
plt.show()


# Interactive Line Chart: Sales over Months
fig_line = px.line(df, x='Month', y='Sales', markers=True, title='Interactive Sales Trend Over Months')
fig_line.update_traces(line_color='#2a9d8f')
fig_line.show()

# Interactive Bar Chart: Sales by Category
fig_bar = px.bar(df, x='Category', y='Sales', text='Sales', title='Interactive Sales by Category', color='Category', color_discrete_sequence=px.colors.qualitative.Set2)
fig_bar.show()

# Interactive Pie Chart: Proportion of Sales by Category
fig_pie = px.pie(df, values='Sales', names='Category', title='Interactive Sales Proportion by Category', color_discrete_sequence=px.colors.qualitative.Set2)
fig_pie.show()

# Interactive Scatter Plot: Sales vs. Profit
fig_scatter = px.scatter(df, x='Sales', y='Profit', text='Category', title='Interactive Sales vs. Profit', color='Category', color_discrete_sequence=px.colors.qualitative.Set2)
fig_scatter.show()