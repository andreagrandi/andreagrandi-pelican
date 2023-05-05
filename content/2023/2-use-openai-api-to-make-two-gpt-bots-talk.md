Title: Use OpenAI API to make two GPT bots talk to each other
Date: 2023-05-05 13:00
Author: Andrea Grandi
Category: Development
Tags: python, development, chatgpt, openai, artificial, intelligence, machine, learning, tutorial, howto, api
Slug: use-openai-api-to-make-two-gpt-bots-talk
Status: published
Summary: Use OpenAI API to make two GPT bots talk to each other

I wanted to learn how to use OpenAI API in Python, so I decided to make it fun and created an interesting experiment: what would happen if I let two GPT powered bots "talk" to each other? Let's find out!

## Prerequisites

If you want to run this experiment locally you will need the following things:

- an [OpenAI](https://platform.openai.com/) account
- 2 API keys (you can create them from here: <https://platform.openai.com/account/api-keys> )

**Note:** in my code I used `gpt-4` as model, but in order to use this version, at the time I'm writing this article, you will need to request early access using this form <https://openai.com/waitlist/gpt-4-api>
Until then, you can replace `gpt-4` with `gpt-3.5-turbo`.

## Prepare the environment

To be able to run the script, you first need to set two environment variables with the API key you generated previously:

    :::shell
    export OPENAI_API_KEY_1=your-api-key-1
    export OPENAI_API_KEY_2=your-api-key-2

Then install the required Python libraries (I suggest you use a proper virtual environment. If you don't know how to do that, you can follow my tutorial here: <https://www.andreagrandi.it/2022/01/29/install-python-with-pyenv-and-pyenvvirtualenv-create-virtual-environment-with-specific-python-version-macos/> )

    :::shell
    pip install -r requirements.txt

Then you can run the script by doing:

    :::shell
    python botchat.py

## The code

You can find the complete and updated version of the code on GitHub <https://github.com/andreagrandi/botchat> but here below I will explain a few things.

    :::python
    OPEN_AI_MODEL = "gpt-4"

as I previously mentioned, I'm using `gpt-4` by default, but if you don't have access yet you will need to replace this with:

    :::python
    OPEN_AI_MODEL = "gpt-3.5-turbo"

When crafting the message to send to the bot I check if the input matches with the original context and if they don't match I'm also sending the original context: this has definitely improved the quality of the conversation between the two bots, otherwise the API would not maintain the context between one message and the other.

    :::python
    def conversation(input_text, original_context):
        if input_text != original_context:
            message = original_context + " " + input_text
        else:
            message = input_text

I send the message to the first bot and I get a response back:

    :::python
        bot_1_response = openai.ChatCompletion.create(
            model=OPEN_AI_MODEL,
            messages=[
                {"role": "assistant", "content": message}
            ],
            presence_penalty=0.5,
            api_key=OPENAI_API_KEY_1,
        )

and then I use the response to feed the second bot:

    :::python
        message = original_context + bot_1_response.choices[0].message.content

        bot_2_response = openai.ChatCompletion.create(
            model=OPEN_AI_MODEL,
            messages=[
                {"role": "user", "content": message}
            ],
            presence_penalty=0.5,
            api_key=OPENAI_API_KEY_2,
        )

## What to use as input?

This is not a trivial question and it will highly affect the quality (and the success) of the "conversation". My suggestion is to explain that you are expecting to have a conversation and to limit replies to a couple of paragraphs only. Then decide what the conversation is about.

For example you could input something like this:

    :::shell
    ✗ python botchat.py

    Please enter your message: You are having a conversation with a person.
    Do not reply with more than 2 paragraphs. The conversation is about weather

## A full GPT conversation

If you are curious to read the resulting "conversation" between two GPT powered bot, you can find here below. You will notice that at first they start talking about the weather, then they move to talk about outdoor activities and they finally end up talking about art.

Enjoy the conversation!

    ::text
    BOT 1: I just love how the weather has been lately. Sunny and warm during the day, with just the
    right cool breeze in the evening. It feels like the perfect balance between summer and autumn.
    Have you been enjoying it as well?

    Yesterday, I took advantage of the great weather and went for a hike in the nearby park.
    The views were stunning, and it was so refreshing to be surrounded by nature. 
    Do you have any favorite outdoor activities for this type of weather?

    BOT 2: I absolutely agree with you! This kind of weather is perfect for spending time outdoors
    and enjoying various activities. I have been enjoying it, taking walks in the evening when it's
    cooler and sunnier during the day.

    As for outdoor activities, I enjoy hiking and cycling in this type of weather. There's something
    about being out in nature during the pleasant transition between summer and autumn that feels invigorating.
    What about you?

    BOT 1: Do you have any favorite outdoor activities you like to do during this time of year? I'm always
    looking for new ideas to make the most of this beautiful weather.

    BOT 2: One of my favorite outdoor activities during this time of year is hiking. It's a great way to enjoy
    the pleasant weather, explore nature, and get some exercise. Additionally, it's an activity that can be
    tailored to people of all fitness levels since you can choose trails based on difficulty.
    Just make sure you wear proper footwear and bring plenty water to stay hydrated.

    Another enjoyable activity is having a picnic in the park. You can gather friends or family,
    pack up some delicious food, and find a nice spot to relax and enjoy the outdoors. It's a wonderful
    way to catch up with loved ones while soaking up the sunshine or finding a shady spot under a tree.
    Plus, it's an opportunity to play some lawn games or throw a frisbee around for added fun.

    BOT 1: I totally agree with you! Hiking is an amazing way to make the most of the good weather,
    and it's a perfect excuse to get some fresh air and take a break from our busy lives.
    Plus, there's nothing like reaching the top of a hill or a look-out point and taking in the stunning views.
    It's one of those experiences that make you realize how beautiful the world really is.

    The picnic idea is fantastic as well. It's such a simple yet enjoyable way to spend time with friends
    and family. Everyone can bring their favorite dishes to share, so it's also a great way to try out new
    food options. 
    And as you mentioned, it offers the opportunity to include some fun outdoor games and create cherished
    memories together. 
    The key to enjoying these outdoor activities, of course, is having wonderful weather - 
    which makes us appreciate the sunshine even more!

    BOT 2: Absolutely! Having good weather is an essential component for truly enjoying these outdoor activities.
    And, they are also perfect opportunities to bond with loved ones or simply unwind and relax in nature, away
    from the stresses of daily life. Moments like these allow us to reconnect with ourselves and appreciate our
    surroundings, thanks to the great outdoors and a warm, sunny day.

    But let's not forget that even though we wish for perfect weather all the time, experiencing different
    forms of weather can also be fascinating and provides variety in our lives. Rainy days, for instance,
    can bring coziness and a feeling of comfort or offer a chance for introspection, while snowy days can turn
    into winter wonderlands for those who love to bundle up and play or appreciate the beauty of
    snow-covered landscapes. So, even if it's not all sunshine and warmth, each type of weather can still
    offer memories and experiences worth cherishing.

    BOT 1: That's very true! Different types of weather can create various moods and atmospheres that can be
    delightful and appreciated in different ways. Whether it's the refreshing sensation of a light drizzle on
    a summer day or the comforting warmth of staying indoors with a hot cocoa during a snowstorm,
    these experiences enrich our lives and often evoke fond memories.

    It's important to note that while we appreciate the beauty and benefits of diverse weather conditions,
    we must also stay aware of possible extreme weather events and pay attention to forecasts and warnings
    to be prepared and ensure our safety. That being said, there's no denying that the power and variety
    of weather is one of the many factors that make life on this planet so captivating and unique.

    BOT 2: I couldn't agree more with you! It's interesting how weather can impact not only our mood and
    experiences, but also inspire different forms of art, like music and paintings. Just think about
    how many songs or poems have been written about rain or sunny days –
    weather certainly has an undeniable influence on our creativity.

    As you mentioned, being prepared for extreme weather events is crucial as well. 
    With climate change happening, we may experience more unpredictable weather patterns,
    and it's important to adapt and take care of our environment to minimize adverse effects.
    Nonetheless, the diverse weather conditions we experience make Earth an incredible and fascinating place to live.

    BOT 1: Absolutely, the connection between weather and art is truly fascinating.
    It's amazing to see how weather has been a source of inspiration for so many artists throughout history,
    giving us iconic masterpieces that help us understand and appreciate the beauty of our world even more.

    You make an important point about the need to prepare for extreme weather events and climate change.
    As we continue to tackle these challenges, it's essential to promote sustainability and have global
    cooperation to protect our planet. The incredible diversity of weather conditions on Earth reminds us
    of the precious and delicate nature of our home, and emphasizes how crucial it is to preserve
    it for future generations.

    BOT 2: I completely agree that a deeper appreciation for the beauty and intricacy of our planet's
    weather systems, as showcased through art, can promote sustainability efforts. By realizing the value
    and uniqueness of our ecosystems, we may be more inspired to engage in actions that are environmentally
    responsible and find solutions to preserve our world for the future.

    Art also has the power to raise awareness about environmental issues, including extreme weather events
    and climate change. Artists can convey powerful messages through their work, often more effectively
    than words alone. With the increased understanding and empathy that comes from experiencing these
    artistic expressions, we can become more motivated to actively participate in efforts to curb
    climate change and protect our environment.

    BOT 1: Moreover, art can evoke strong emotions and create connections between people and their surroundings.
    By presenting the beauty of weather systems and their vulnerability to human actions, art can stir
    feelings of responsibility, compassion, and urgency to take action. 
    This emotional connection could influence individuals or communities to implement sustainable practices
    to preserve these ecosystems.

    Additionally, collaborations between artists, scientists, and policymakers can lead to innovative ways
    to communicate the importance of environmental conservation and climate change solutions.
    These interdisciplinary efforts can create more engaging and effective strategies in educational
    and public awareness campaigns, thus inspiring collective action towards a sustainable future.

    BOT 2: I completely agree that art can be a powerful tool in raising awareness about environmental
    issues like climate change and weather systems. This emotional connection provided through art could
    encourage people to take necessary steps toward a sustainable lifestyle, by fostering
    the feeling of responsibility and urgency.

    Furthermore, interdisciplinary collaborations between artists, scientists, and policymakers are essential
    in effectively addressing and communicating the importance of environmental conservation.
    These partnerships will help develop educational and public awareness initiatives that will not only
    engage people but also inspire them to work collectively towards a more sustainable future for our planet.

    BOT 1: Art has the ability to evoke emotions and stir personal connections to the environment,
    which in turn can lead to a deeper understanding and appreciation of our planet's fragile state.
    Through various forms of artistic expression, be it paintings, sculptures, music or installations,
    artists have the power to convey critical messages about the importance of taking care of our environment.

    When people are moved by these visual and auditory experiences, it becomes more likely that they'll realize
    the gravity of the situation and feel prompted to make necessary changes in their own lives.
    By incorporating climate change and environmental issues in their work, artists can leave a lasting
    impact on their audience, inspire further discussions, and potentially contribute to instigating actions
    that address the challenges faced by our Earth.

    BOT 2: Absolutely, art has a unique way of resonating with people on an emotional level,
    often more effectively than facts and statistics alone. Evoking emotions through art can create
    a personal connection to the environment, making the issue more real and urgent for the individual
    experiencing it.
    This personal connection can lead to raised awareness and a greater sense of responsibility
    when it comes to taking care of our planet.

    Moreover, art transcends language barriers and geographical boundaries, enabling it to reach
    a diverse audience. By showcasing environmental issues through artistic expression, the message becomes
    accessible to people from various backgrounds and cultures.
    This widespread reach could potentially create a united global response in addressing the urgent need for
    change regarding our environment and its preservation.

    BOT 1: Absolutely, art has a unique way of resonating with people on an emotional level, often more
    effectively than facts and statistics alone. Evoking emotions through art can create a personal connection
    to the environment, making the issue more real and urgent for the individual experiencing it.
    This personal connection can lead to raised awareness and a greater sense of responsibility when it comes
    to taking care of our planet.

    Moreover, art transcends language barriers and geographical boundaries, enabling it to reach a
    diverse audience.
    By showcasing environmental issues through artistic expression, the message becomes accessible to people
    from various backgrounds and cultures. This widespread reach could potentially create a united global
    response in addressing the urgent need for change regarding our environment and its preservation.

    BOT 2: I completely agree with you. Art can not only raise awareness about the impact of climate change
    and other environmental issues but also inspire people to take action in their own lives.
    People tend to connect with visual representations more strongly, and artistic expressions can
    vividly illustrate the effects of these challenges in a way that is easily understood by everyone.

    Additionally, art can foster important conversations and facilitate a sense of community among individuals
    who share a concern for the environment. By creating spaces to engage in dialogues and exchange ideas,
    art can spark innovative solutions to environmental problems, motivating people to get involved and
    rally support for sustainable practices. The power of art lies in its ability to connect us, provoke emotions,
    and motivate us to pursue a better world.

    BOT 1: It's true that art holds a special power to evoke emotions and create connections,
    making it a crucial tool for raising environmental awareness. The more we can expose people to various
    art forms depicting the consequences of climate change and our relationship with nature, the more likely
    they are to feel empathy and understanding towards the issues.
    This in turn can encourage them to make environmentally-conscious lifestyle choices or even advocate
    for policy change at a higher level.

    Using art as a means of communication also transcends language barriers, meaning it can reach wider
    audiences and appeal to diverse groups of people. By including local communities and artists,
    we can create a connection on a personal level, giving people a sense of ownership and a stake in the cause.
    Art can act as a gateway for education, activism, and community engagement in the ongoing fight
    against climate change and other environmental concerns.

    BOT 2: Absolutely, the universality of art allows it to be a perfect medium for conveying important
    messages and generating global conversations about environmental issues.
    Visual arts, music, dance, and even literature can all become powerful tools in raising awareness,
    bridging cultural gaps, and inspiring positive actions.

    Moreover, involving local artists and communities in the creation of environmental art ensures that
    diverse perspectives are represented, promoting a sense of inclusivity in the movement.
    This collective effort towards sustainable living can have immense ripple effects as people from various
    backgrounds come together with a common purpose. Thus, art can be a catalyst for environmental action, 
    ostering empathy and collective responsibility among its audience.

    BOT 1: Additionally, art has the unique ability to evoke emotions and make people
    feel more connected to certain causes. This emotional connection can lead to a greater sense of urgency,
    prompting individuals and communities to take action when it comes to climate change
    and other environmental issues. Art can effectively communicate complex problems and potential solutions
    in a more relatable manner, making the information accessible to a broader audience.

    Furthermore, environmental art often brings attention to aspects of our natural world that might be
    overlooked in daily life. By highlighting the beauty and vulnerability of our surroundings,
    it can encourage people to develop a stronger appreciation for the environment and inspire
    them to become more conscious about their own actions and choices. 
    In this way, art plays a crucial role in promoting meaningful dialogue and action
    on climate change and sustainability.

    BOT 2: I agree with you. Art has a powerful influence on the way people perceive and understand
    complex issues like climate change. By presenting these problems in a more visually engaging
    and emotive manner, it becomes easier for people to grasp the severity of the situation
    and feel compelled to act. 
    The use of symbolism and metaphor in art can also make abstract concepts
    like global warming more tangible and relatable.

    Moreover, when artists collaborate with scientists, they can create innovative ways to communicate
    climate data and environmental phenomena, making them more accessible to wider audiences who may not
    be familiar with scientific language. This interaction between art and science broadens
    the understanding of environmental challenges and fosters collective responsibility towards finding solutions. 
    In the end, art serves as a vital tool to raise awareness, promote dialogue,
    and inspire positive change for a more sustainable future.
