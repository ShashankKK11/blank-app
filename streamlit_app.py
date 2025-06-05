import streamlit as st


MENU = {
    "Pizza": 250,
    "Burger": 150,
    "Pasta": 200,
    "Salad": 120,
    "Sushi": 300,
    "Tacos": 180
}

def main():
    st.title("🍽️ Food Service App")

    st.header("Menu")
    for dish, price in MENU.items():
        st.write(f"**{dish}** - ₹{price}")

    st.header("Order Your Food")
    selected_dishes = st.multiselect("Select dishes to order:", list(MENU.keys()))

    if selected_dishes:
        total = sum([MENU[dish] for dish in selected_dishes])
        st.write(f"**Total: ₹{total}**")
    else:
        st.write("No items selected yet.")

    if st.button("Place Order"):
        if selected_dishes:
            st.success(f"Order placed for: {', '.join(selected_dishes)}. Total amount: ₹{total}")
        else:
            st.warning("Please select at least one item to place an order.")

if __name__ == "__main__":
    main()
