// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class KeepUserTags extends TeaModel {
    @NameInMap("all")
    public Boolean all;

    @NameInMap("keys")
    public java.util.List<String> keys;

    public static KeepUserTags build(java.util.Map<String, ?> map) throws Exception {
        KeepUserTags self = new KeepUserTags();
        return TeaModel.build(map, self);
    }

    public KeepUserTags setAll(Boolean all) {
        this.all = all;
        return this;
    }
    public Boolean getAll() {
        return this.all;
    }

    public KeepUserTags setKeys(java.util.List<String> keys) {
        this.keys = keys;
        return this;
    }
    public java.util.List<String> getKeys() {
        return this.keys;
    }

}
