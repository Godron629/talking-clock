import os
import pyaudio
import wave
import datetime


class TalkingClock(object):

    number_to_word = {
        0: " twelve",
        1: " one",
        2: " two",
        3: " three",
        4: " four",
        5: " five",
        6: " six",
        7: " seven",
        8: " eight",
        9: " nine",
        10: " ten",
        11: " eleven",
        12: " twelve",
        13: " thirteen",
        14: " fourteen",
        15: " fifteen",
        16: " sixteen",
        17: " seventeen",
        18: " eighteen",
        19: " nineteen",
        20: " twenty",
        30: " thirty",
        40: " fourty",
        50: " fifty",
    }

    tens_to_word = {
        2: " twenty",
        3: " thirty",
        4: " fourty",
        5: " fifty",
    }

    def talking_clock(self, time):
        try:
            hour, minutes = [int(x) for x in time.split(":")]
        except ValueError: 
            raise ValueError("Time not in format 'HH:MM'")

        output = "It's"
        output += self.number_to_word[hour % 12]

        period = " am" if (hour % 24 < 12) else " pm"
        minutes = minutes % 60

        if minutes == 0:
            pass
        elif minutes < 20:
            output += (" oh" if minutes < 10 else "") + self.number_to_word[minutes]
        else:
            tens, ones = divmod(minutes, 10)
            output += self.tens_to_word[tens]

            if minutes % 10:
                output += self.number_to_word[ones]

        return output + period 

    def time_to_speech(self, sentance):
        word_to_number = {v[1:]: str(k) for k, v in self.number_to_word.iteritems()}

        directory = os.path.dirname(os.path.realpath(__file__))

        sentance = sentance.split()

        sounds_to_play = ["its"]
        am_or_pm = sentance[-1]

        if len(sentance) == 3:
            sounds_to_play.append(word_to_number[sentance[1]])

        elif len(sentance) == 4:
            sounds_to_play.append(word_to_number[sentance[1]])

            if sentance[2].endswith("ty"):
                sounds_to_play.append(sentance[2].split("ty")[0])
                sounds_to_play.append("ty")

            elif sentance[2].endswith("teen"):
                sounds_to_play.append(sentance[2].split("teen")[0])
                sounds_to_play.append("teen")

            else: 
                sounds_to_play.append(word_to_number[sentance[2]])
                

        elif len(sentance) == 5:
            sounds_to_play.append(word_to_number[sentance[1]])

            if sentance[2].endswith("ty"):
                sounds_to_play.append(sentance[2].split("ty")[0])
                sounds_to_play.append("ty")

            elif sentance[2] == "oh":
                sounds_to_play.append("o")

            sounds_to_play.append(word_to_number[sentance[3]])

        sounds_to_play.append(am_or_pm)

        for i in sounds_to_play:
            self.play_sounds(os.path.join(directory, "sound_clips", i + ".wav"))


    @staticmethod
    def play_sounds(sound_path):
        chunk = 1024
        f = wave.open(sound_path, "rb")
        p = pyaudio.PyAudio()

        stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                        channels=f.getnchannels(),
                        rate = f.getframerate(),
                        output=True)

        data = f.readframes(chunk)

        while data: 
            stream.write(data)
            data = f.readframes(chunk)

        stream.stop_stream()
        stream.close()
        p.terminate()


if __name__ == '__main__':
    talker = TalkingClock()

    time = datetime.datetime.now().strftime("%H:%M")

    sentance = talker.talking_clock(time)
    talker.time_to_speech(sentance)

