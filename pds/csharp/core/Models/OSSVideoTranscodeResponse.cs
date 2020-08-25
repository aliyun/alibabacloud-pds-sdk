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
    public class OSSVideoTranscodeResponse : TeaModel {
        /// <summary>
        /// definition_list
        /// </summary>
        [NameInMap("definition_list")]
        [Validation(Required=false)]
        public List<string> DefinitionList { get; set; }

        /// <summary>
        /// duration
        /// </summary>
        [NameInMap("duration")]
        [Validation(Required=false)]
        public long Duration { get; set; }

        /// <summary>
        /// hls_time
        /// </summary>
        [NameInMap("hls_time")]
        [Validation(Required=false)]
        public long HlsTime { get; set; }

    }

}
