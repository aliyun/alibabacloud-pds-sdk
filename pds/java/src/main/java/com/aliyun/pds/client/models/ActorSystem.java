// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 *
 */
public class ActorSystem extends TeaModel {
    // EventType
    @NameInMap("event_type")
    public String eventType;

    public static ActorSystem build(java.util.Map<String, ?> map) throws Exception {
        ActorSystem self = new ActorSystem();
        return TeaModel.build(map, self);
    }

    public ActorSystem setEventType(String eventType) {
        this.eventType = eventType;
        return this;
    }
    public String getEventType() {
        return this.eventType;
    }

}
