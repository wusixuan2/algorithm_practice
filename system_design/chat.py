'''
Definition of PushNotification
class PushNotification:
    @classmethod
    def notify(user_id, message):
'''
class PubSubPattern:
    channel_id = {}
    def __init__(self):
        pass
    # do intialization if necessary

    """
    @param: channel: a channel name
    @param: user_id: a user id
    @return: nothing
    """
    def subscribe(self, channel, user_id):
        if channel not in self.channel_id:
            self.channel_id[channel] = set()
        self.channel_id[channel].add(user_id)

    """
    @param: channel: a channel name
    @param: user_id: a user id
    @return: nothing
    """

    def unsubscribe(self, channel, user_id):
        if channel in self.channel_id and user_id in self.channel_id[channel] :
          self.channel_id[channel].remove(user_id)

    """
    @param: channel: a channel name
    @param: message: need send message
    @return: nothing
    """

    def publish(self, channel, message):
        if channel in self.channel_id and len(self.channel_id[channel]) != 0:
            for id in self.channel_id[channel] :
                PushNotification.notify(id, message)
