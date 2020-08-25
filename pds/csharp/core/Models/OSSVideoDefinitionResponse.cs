// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.PDS.Client.Models
{
    /**
     * 转码接口response
     */
    public class OSSVideoDefinitionResponse : TeaModel {
        /// <summary>
        /// definition_list
        /// </summary>
        [NameInMap("definition_list")]
        [Validation(Required=false)]
        public List<string> DefinitionList { get; set; }

        /// <summary>
        /// frame_rate
        /// </summary>
        [NameInMap("frame_rate")]
        [Validation(Required=false)]
        public string FrameRate { get; set; }

    }

}
