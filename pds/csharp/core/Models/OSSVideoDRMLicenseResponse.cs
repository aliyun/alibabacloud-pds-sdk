// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.PDS.Client.Models
{
    /**
     * DRM License response
     */
    public class OSSVideoDRMLicenseResponse : TeaModel {
        /// <summary>
        /// drm_data
        /// </summary>
        [NameInMap("data")]
        [Validation(Required=true)]
        public string Data { get; set; }

        /// <summary>
        /// states
        /// </summary>
        [NameInMap("states")]
        [Validation(Required=true)]
        public long? States { get; set; }

    }

}
