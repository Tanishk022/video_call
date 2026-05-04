# import streamlit as st
# from streamlit_webrtc import webrtc_streamer, WebRtcMode, RTCConfiguration

# st.title("Doctor-Patient Video Call")

# room_id = st.text_input("Enter Room ID")

# if room_id:
#     webrtc_streamer(
#         key=room_id,
#         mode=WebRtcMode.SENDRECV,
#         rtc_configuration=RTCConfiguration({
#             "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
#         }),
#         media_stream_constraints={
#             "video": True,
#             "audio": True
#         }
#     )

# import streamlit as st
# from streamlit_webrtc import webrtc_streamer, WebRtcMode, RTCConfiguration
# import uuid

# st.set_page_config(page_title="Doctor-Patient Video Call", layout="centered")

# st.title("🩺 Doctor - Patient Video Consultation")

# # ---------- SESSION STATE ----------
# if "room_id" not in st.session_state:
#     st.session_state.room_id = ""

# # ---------- CREATE ROOM ----------
# st.subheader("Create or Join Consultation")

# col1, col2 = st.columns(2)

# with col1:
#     if st.button("🆕 Create New Room"):
#         st.session_state.room_id = str(uuid.uuid4())[:8]
#         st.success(f"Room Created! Share this ID:\n\n{st.session_state.room_id}")

# with col2:
#     join_id = st.text_input("Enter Room ID")
#     if st.button("🔗 Join Room"):
#         if join_id:
#             st.session_state.room_id = join_id
#         else:
#             st.warning("Please enter a valid Room ID")

# # ---------- SHOW CURRENT ROOM ----------
# if st.session_state.room_id:
#     st.markdown(f"### 🔑 Current Room ID: `{st.session_state.room_id}`")

#     st.info("👉 Doctor and Patient must use the SAME Room ID to connect.")

#     # ---------- WEBRTC CONFIG ----------
#     rtc_config = RTCConfiguration({
#         "iceServers": [
#             {"urls": ["stun:stun.l.google.com:19302"]},
#             {
#                 "urls": ["turn:openrelay.metered.ca:80"],
#                 "username": "openrelayproject",
#                 "credential": "openrelayproject"
#             }
#         ]
#     })

#     # ---------- VIDEO CALL ----------
#     webrtc_streamer(
#         key=st.session_state.room_id,
#         mode=WebRtcMode.SENDRECV,
#         rtc_configuration=rtc_config,
#         media_stream_constraints={
#             "video": True,
#             "audio": True
#         },
#         async_processing=True,
#     )

#     st.success("✅ Video Call Ready! Ask the other person to join with the same Room ID.")


# import streamlit as st
# from streamlit_webrtc import webrtc_streamer, WebRtcMode, RTCConfiguration
# import uuid
# import logging

# # 🔥 Fix logging issue
# logging.basicConfig(level=logging.WARNING)

# st.set_page_config(page_title="Doctor-Patient Video Call", layout="centered")

# st.title("🩺 Doctor - Patient Video Consultation")

# # ---------- SESSION STATE ----------
# if "room_id" not in st.session_state:
#     st.session_state.room_id = ""

# # ---------- CREATE ROOM ----------
# st.subheader("Create or Join Consultation")

# col1, col2 = st.columns(2)

# with col1:
#     if st.button("🆕 Create New Room"):
#         st.session_state.room_id = str(uuid.uuid4())[:8]
#         st.success(f"Room Created! Share this ID:\n\n{st.session_state.room_id}")

# with col2:
#     join_id = st.text_input("Enter Room ID")
#     if st.button("🔗 Join Room"):
#         if join_id:
#             st.session_state.room_id = join_id
#         else:
#             st.warning("Please enter a valid Room ID")

# # ---------- SHOW CURRENT ROOM ----------
# if st.session_state.room_id:
#     st.markdown(f"### 🔑 Current Room ID: `{st.session_state.room_id}`")

#     st.info("👉 Doctor and Patient must use the SAME Room ID to connect.")

#     # 🔥 STRONG RTC CONFIG (STUN + MULTIPLE TURN)
#     rtc_config = RTCConfiguration({
#         "iceServers": [
#             {"urls": ["stun:stun.l.google.com:19302"]},
#             {
#                 "urls": [
#                     "turn:openrelay.metered.ca:80",
#                     "turn:openrelay.metered.ca:443",
#                     "turn:openrelay.metered.ca:443?transport=tcp"
#                 ],
#                 "username": "openrelayproject",
#                 "credential": "openrelayproject"
#             }
#         ]
#     })

#     # ---------- VIDEO CALL ----------
#     webrtc_streamer(
#         key=st.session_state.room_id,
#         mode=WebRtcMode.SENDRECV,
#         rtc_configuration=rtc_config,
#         media_stream_constraints={
#             "video": True,
#             "audio": True
#         },
#         async_processing=False  # 🔥 FIX (IMPORTANT)
#     )

#     st.success("✅ Video Call Ready! Ask the other person to join with the same Room ID.")




import streamlit as st
import uuid

st.set_page_config(page_title="Doctor Video Call", layout="wide")

st.title("🩺 Doctor - Patient Video Consultation")

# ---------- SESSION ----------
if "room_id" not in st.session_state:
    st.session_state.room_id = ""

# ---------- CREATE / JOIN ----------
col1, col2 = st.columns(2)

with col1:
    if st.button("🆕 Create Room"):
        st.session_state.room_id = str(uuid.uuid4())[:8]
        st.success(f"Room ID: {st.session_state.room_id}")

with col2:
    join_id = st.text_input("Enter Room ID")
    if st.button("🔗 Join Room"):
        if join_id:
            st.session_state.room_id = join_id

# ---------- VIDEO CALL ----------
if st.session_state.room_id:
    room = st.session_state.room_id

    st.markdown(f"### 🔑 Room ID: `{room}`")
    st.info("👉 Share this Room ID with doctor/patient")

    jitsi_url = f"https://meet.jit.si/{room}"

    st.markdown(
        f"""
        <iframe
            src="{jitsi_url}"
            width="100%"
            height="600"
            allow="camera; microphone; fullscreen; display-capture"
        ></iframe>
        """,
        unsafe_allow_html=True
    )