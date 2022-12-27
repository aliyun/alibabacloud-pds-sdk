// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class UserTag extends TeaModel {
    /**
     * <p>key</p>
     */
    @NameInMap("key")
    public String key;

    /**
     * <p>value</p>
     */
    @NameInMap("value")
    public String value;

    public static UserTag build(java.util.Map<String, ?> map) throws Exception {
        UserTag self = new UserTag();
        return TeaModel.build(map, self);
    }

    public UserTag setKey(String key) {
        this.key = key;
        return this;
    }
    public String getKey() {
        return this.key;
    }

    public UserTag setValue(String value) {
        this.value = value;
        return this;
    }
    public String getValue() {
        return this.value;
    }

}
