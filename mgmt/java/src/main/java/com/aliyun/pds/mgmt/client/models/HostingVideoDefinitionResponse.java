// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 转码接口response
 */
public class HostingVideoDefinitionResponse extends TeaModel {
    /**
     * <p>definition_list</p>
     */
    @NameInMap("definition_list")
    public java.util.List<String> definitionList;

    /**
     * <p>frame_rate</p>
     */
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
