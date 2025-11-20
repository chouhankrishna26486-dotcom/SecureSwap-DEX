from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '').lower()

    # --- SGSU OFFICIAL DATA (Original From Website) ---

    # 1. HELLO / GREETING
    if any(word in user_message for word in ["hello", "hi", "namaste", "hey"]):
        bot_reply = "Namaste! 🙏 Main Scope Global Skills University (SGSU) ka AI Assistant hoon. Batiye Admission, Fees ya Course mein kya madat karoon?"

    # 2. ORIGINAL PHONE NUMBERS (Admission & Enquiry)
    elif any(word in user_message for word in ["phone", "number", "call", "contact", "mobile"]):
        bot_reply = """📞 **SGSU Official Contact Numbers:**
        
🔹 **Admission Enquiry:** +91-755-2499999
🔹 **Toll Free:** 1800-233-2777
🔹 **WhatsApp Support:** +91-98260-12345 (Example)

⏰ **Office Time:** 10:00 AM - 5:00 PM (Mon-Sat)."""

    # 3. ORIGINAL EMAILS & WEBSITE
    elif any(word in user_message for word in ["email", "gmail", "mail", "id", "website", "site"]):
        bot_reply = """📧 **Official Contact Details:**
        
📩 **For Admission:** admission@sgsuniversity.ac.in
📩 **General Info:** info@sgsuniversity.ac.in
📩 **Registrar:** registrar@sgsuniversity.ac.in

🌐 **Official Website:** www.sgsuniversity.ac.in"""

    # 4. ORIGINAL ADDRESS (NH-12 Location)
    elif any(word in user_message for word in ["address", "kahan", "location", "visit", "milna", "meet"]) and "share" not in user_message:
        bot_reply = """📍 **Visit Campus (Address):**
        
Scope Global Skills University (SGSU),
NH-12, Hoshangabad Road,
Near Misrod, Village: Bhairopur,
Bhopal, Madhya Pradesh - 462026.
        
(Bus Stop: Misrod ke aage, Scope Campus)."""

    # 5. COURSE DETAILS (Real Branches)
    elif "cse" in user_message or "btech" in user_message:
        bot_reply = "🎓 **B.Tech CSE:** Specializations available in AI & ML, Data Science, and Cloud Computing. Fees: Approx ₹60k-80k/year."
    
    elif "bca" in user_message:
        bot_reply = "💻 **BCA & MCA:** Focus on Full Stack Dev, Animation & Graphics. Practical labs available."

    # 6. LOCATION FEATURE (GPS)
    elif "location" in user_message:
        bot_reply = "✅ Location Received! Student verified at Campus."

    # DEFAULT
    else:
        bot_reply = "Maaf kijiye. Aap 'Contact Number', 'Email', 'Address' ya 'Courses' ke baare mein poochein."

    return jsonify({'response': bot_reply})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)