import streamlit as st

st.markdown("## streamlite 组件使用")
st.markdown("---")
r12c1,r12c2 = st.columns(2)
with r12c1:
    st.markdown("##### (1)st.button 按钮")
    if st.button("点我！"):
        "点击了按钮"
with r12c2:
    st.markdown("##### (2) st.checkbox 检查框")
    if st.checkbox("打勾了吗？"):
        "选中啦！"
    else:
        "没选中。"
st.markdown("---")

r22c1,r22c2 = st.columns(2)
with r22c1:
    st.markdown("##### (3) st.radio 单项选择框")
    my_radio = st.radio("你最喜欢哪首歌？",
                   ("pachka sigaret","gruppa krovi","zvezda pa imeni solntse"))
    if my_radio:
        f"我最喜欢{my_radio}"
with r22c2:
    st.markdown("##### (4) st.selectbox 下拉选择框")
    my_selectbox = st.selectbox("Which song do you like most？",
                    ("pachka sigaret","gruppa krovi","zvezda pa imeni solntse"))
    if my_selectbox:
        f"I like {my_selectbox} most."
st.markdown("---")

r32c1,r32c2 = st.columns(2)
with r32c1:
    st.markdown("##### (5) st.multiselect 多项选择框")
    my_multiselect = st.multiselect("选择你喜欢的歌",
                            options=("《一包香烟》","《血型》","《名为太阳的星辰》"),
                            default=("《一包香烟》","《血型》"))
    if my_multiselect:
        f"我喜欢 {'、'.join(i for i in my_multiselect)}。"
with r32c2:
    st.markdown("##### st.text_area 多行文本框")
    st.text_area("Text Area Height = 150 pixels",
             f"{' '.join(str(i) for i in range(200))}",
             height=150)
st.markdown("---")

r42c1,r42c2 = st.columns(2)
with r42c1:
    st.markdown("##### (7)st.slider & st.select_slider 滑杆、选项滑杆")
    # 滑杆
    my_slider = st.slider("计算平方数",0,100,50,1)
    if my_slider:
        f"{my_slider}的平方是{my_slider ** 2}"
    # 选项滑杆
    transdict = {"Red":"红","Orange":"橙","Yellow":"黄",
                "Green":"绿","Blue":"蓝","Purple":"紫"}
    my_select_slider = st.select_slider("Choose Your Favorite Color！",
                            ("Red","Orange","Yellow","Green","Blue","Purple"),"Red")
    if my_select_slider:
        f"你选择了{transdict[my_select_slider]}色！"
with r42c2:
    st.markdown("##### (8) st.text_input, st.number_input, st.date_input, st.time_input 信息输入")
    st.text_input("这是TEXT_INPUT")
    st.number_input("这是NUMBER_INPUT",value=10)
    st.date_input("这是DATE_INPUT")
    st.time_input("这是TIME_INPUT")
st.markdown("---")

r52c1,r52c2 = st.columns(2)
with r52c1:
    st.markdown("##### (9) st.download_button 下载按钮")
    import pandas as pd
    # 示例数据
    data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
    }
    my_large_df = pd.DataFrame(data)
    # 1
    @st.cache_data
    def convert_df(df):
        return df.to_csv().encode('utf-8')    
    csv = convert_df(my_large_df)
    st.download_button(label="Download data as CSV", 
                    data=csv, file_name='large_df.csv', mime='text/csv')
    # 2
    text_contents = '''This is some text'''
    st.download_button('Download some text', text_contents)
    # 3
    binary_contents = b'example content'
    # MIME default as 'application/octet-stream'
    st.download_button('Download binary file', binary_contents)
    # 4
    with open("flower.png", "rb") as file:
        btn = st.download_button(label="Download image",
                        data=file,file_name="flower.png",mime="image/png")
    
with r52c2:
    st.markdown("##### (10) st.file_uploader 文件上传")
    # 上传单个文件 Upload single file
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        # To read file as bytes:
        bytes_data = uploaded_file.getvalue()
        st.write(bytes_data)

        # To convert to a string based IO:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        st.write(stringio)

        # To read file as string:
        string_data = stringio.read()
        st.write(string_data)

        # Can be used wherever a "file-like" object is accepted:
        dataframe = pd.read_csv(uploaded_file)
        st.write(dataframe)
    #上传多个文件 Upload multi files
    uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        st.write("filename:", uploaded_file.name)
        st.write(bytes_data)
st.markdown("---")
