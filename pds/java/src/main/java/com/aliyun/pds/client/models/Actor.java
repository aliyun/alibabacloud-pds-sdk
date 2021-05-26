// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class Actor extends TeaModel {
    @NameInMap("ali_user")
    public ActorAliUser aliUser;

    @NameInMap("anonymous_user")
    public ActorAnonymousUser anonymousUser;

    @NameInMap("system")
    public ActorSystem system;

    @NameInMap("user")
    public ActorUser user;

    public static Actor build(java.util.Map<String, ?> map) throws Exception {
        Actor self = new Actor();
        return TeaModel.build(map, self);
    }

    public Actor setAliUser(ActorAliUser aliUser) {
        this.aliUser = aliUser;
        return this;
    }
    public ActorAliUser getAliUser() {
        return this.aliUser;
    }

    public Actor setAnonymousUser(ActorAnonymousUser anonymousUser) {
        this.anonymousUser = anonymousUser;
        return this;
    }
    public ActorAnonymousUser getAnonymousUser() {
        return this.anonymousUser;
    }

    public Actor setSystem(ActorSystem system) {
        this.system = system;
        return this;
    }
    public ActorSystem getSystem() {
        return this.system;
    }

    public Actor setUser(ActorUser user) {
        this.user = user;
        return this;
    }
    public ActorUser getUser() {
        return this.user;
    }

}
