// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class LinkInfo extends TeaModel {
    /**
     * <p>额外的信息，比如type为mobile时，此字段为国家编号，不填默认86</p>
     */
    @NameInMap("extra")
    public String extra;

    /**
     * <p>当前用户已存在的登录标识</p>
     */
    @NameInMap("identity")
    public String identity;

    /**
     * <p>当前用户已存在的登录方式</p>
     */
    @NameInMap("type")
    public String type;

    public static LinkInfo build(java.util.Map<String, ?> map) throws Exception {
        LinkInfo self = new LinkInfo();
        return TeaModel.build(map, self);
    }

    public LinkInfo setExtra(String extra) {
        this.extra = extra;
        return this;
    }
    public String getExtra() {
        return this.extra;
    }

    public LinkInfo setIdentity(String identity) {
        this.identity = identity;
        return this;
    }
    public String getIdentity() {
        return this.identity;
    }

    public LinkInfo setType(String type) {
        this.type = type;
        return this;
    }
    public String getType() {
        return this.type;
    }

}
