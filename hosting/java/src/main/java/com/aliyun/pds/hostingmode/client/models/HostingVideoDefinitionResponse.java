// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.hostingmode.client.models;

import com.aliyun.tea.*;

/**
 * 转码接口response
 */
public class HostingVideoDefinitionResponse extends TeaModel {
    // definition_list
    @NameInMap("definition_list")
    public java.util.List<String> definitionList;

    // frame_rate
    @NameInMap("frame_rate")
    public String frameRate;

    public static HostingVideoDefinitionResponse build(java.util.Map<String, ?> map) throws Exception {
        HostingVideoDefinitionResponse self = new HostingVideoDefinitionResponse();
        return TeaModel.build(map, self);
    }

    public HostingVideoDefinitionResponse setDefinitionList(java.util.List<String> definitionList) {
        this.definitionList = definitionList;
        return this;
    }
    public java.util.List<String> getDefinitionList() {
        return this.definitionList;
    }

    public HostingVideoDefinitionResponse setFrameRate(String frameRate) {
        this.frameRate = frameRate;
        return this;
    }
    public String getFrameRate() {
        return this.frameRate;
    }

}
