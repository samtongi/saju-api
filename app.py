from flask import Flask, request, jsonify
import openai  # OpenAI API 호출

app = Flask(__name__)

# OpenAI API Key 설정 (자신의 키 입력)
openai.api_key = "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"

def get_saju_interpretation(year, month, day, hour):
    prompt = f"""
    사용자의 생년월일: {year}년 {month}월 {day}일, 태어난 시간: {hour}시

    사주팔자를 분석하여 다음 정보를 제공하세요:
    1. 기본적인 사주 해석 (천간·지지, 오행 분석)
    2. 성격 분석 (예: 리더형, 감성형, 분석형)
    3. 직업운 (적합한 직업 추천)
    4. 연애운 및 궁합 (연애 성향 분석)
    5. 2024년~2025년 운세 예측
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "당신은 사주 전문가입니다."},
                  {"role": "user", "content": prompt}]
    )

    return response["choices"][0]["message"]["content"]

@app.route('/saju', methods=['POST'])
def get_saju():
    data = request.json
    year = data.get('year')
    month = data.get('month')
    day = data.get('day')
    hour = data.get('hour')

    if not (year and month and day and hour):
        return jsonify({"error": "생년월일시를 입력해주세요"}), 400

    result = get_saju_interpretation(year, month, day, hour)
    return jsonify({"saju_result": result})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
