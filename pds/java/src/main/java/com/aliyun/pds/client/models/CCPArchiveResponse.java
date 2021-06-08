// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class CCPArchiveResponse extends TeaModel {
    @NameInMap("state")
    public String state;

    public static CCPArchiveResponse build(java.util.Map<String, ?> map) throws Exception {
        CCPArchiveResponse self = new CCPArchiveResponse();
        return TeaModel.build(map, self);
    }

    public CCPArchiveResponse setState(String state) {
        this.state = state;
        return this;
    }
    public String getState() {
        return this.state;
    }

}
