## Recipe Website
___

### Problem
Finding and selecting meals and their recipes with the current spreadsheet method takes too much time. The same thing goes for determining what ingredients are needed for the selected recipes and compiling a shopping list. The biggest annoyance is that there are multiple websites that must be opened at one time to achieve a grocery list, and again opened once the meals are to be cooked.
- The spreadsheet only contains links to the recipe websites.
- Each meal website must be manually parsed for ingredients and recipes.
- Grocery lists must be manually put together by going through every meal website's ingredients list.  

**The current process for adding a new recipe to the Bad Bitches Meal Prep Google Sheet is as follows:**
  - Copy and paste recipe link into the next available empty cell in column A.
  - Format the cell into a custom hyperlink.
  - Edit remainder columns as needed.

**The current process for finding recipes and putting together shopping lists is as follows:**
  - Open Bad Bitches Meal Prep Google Sheet.
  - Open the website for each meal that is chosen
  - Open HEB website.
  - Scroll to ingredients list on the meal website.
  - Determine servings and ingredients as needed.
   **Note:** *Some recipes do not have correct servings for us, so the ingredients have to be manually calculated.*
  - Search for needed ingredients on HEB and add to cart.
  **Note:** *It is common to compare prices at different stores such as HEB and Costco.*
  - Repeat previous steps for every meal.

  - **Finally,** each selected meal's website must be opened again at the time of cooking in order to view recipes. 
  **Note:** *Some recipes do not have correct servings for us, so the ingredients have to be manually calculated.*

### Purpose
The purpose of this application is to localize meals and consolidate their respective information and tasks in one place.

**Example processes:**
- New meals can be added to the website by uploading their URL via GUI.
- A list of added meals can be seen and filtered.
- Selecting a meal will reveal buttons that will allow the following:
  - **Add to Cart:** Adds the meal to the cart.
  - **Info:** See nutrition facts and recipe for meal.
  - **Delete:** Remove the meal from the list of available meals. 
- **Checkout cart:** A list of ingredients and recipes will be compiled into a text document based on the servings selected for each meal.

### Minimum Viable Product:
- Access website anywhere
- Upload, edit, and delete meals
- Sort and filter meals based on parameters
- View recipe info: Nutrition, Ingredients
- Filter meals based on certain parameters
- Add meals to a "cart"
- Checkout cart for a list of ingredients and 

### Future Features:
- User system that will allow users to make comments on meals and save their own favorites.
- AI recipe: AI will generate a set of instructions for *all* recipes that will be cooked that will optimize the prep and cooking process. (See https://goblin.tools)
- Statistics tracking
