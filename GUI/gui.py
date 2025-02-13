page = """
<|layout|columns=250px 1|


<|part|class_name=sidebar|


# Interface

**Select Mode**{: .color-primary}
<|{current_mode}|selector|lov=Cloud LLM;Secure Cloud LLM;On-Device LLM;Auto Prompt Routing|>
<|Reset Conversation|button|class_name=fullwidth align-item-bottom plain|id=reset_app_button|on_action=reset_chat|>
|>



<|part|class_name=p2 align-item-bottom table|
<|{conversation}|table|style=style_conv|show_all|selected={selected_row}|rebuild|>
<|part|class_name=card mt1|
<|{current_user_message}|input|label=Write your message here...|on_action=send_message|class_name=fullwidth|change_delay=-1|>
|>
|>


|>
"""


