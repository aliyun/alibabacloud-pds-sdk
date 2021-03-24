// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.PDS.Client.Models
{
    /**
     * GetOfficeEditUrlWatermark 水印配置
     */
    public class GetOfficeEditUrlWatermark : TeaModel {
        /// <summary>
        /// FillStyle
        /// </summary>
        [NameInMap("fillstyle")]
        [Validation(Required=false)]
        public string Fillstyle { get; set; }

        /// <summary>
        /// Font
        /// </summary>
        [NameInMap("font")]
        [Validation(Required=false)]
        public string Font { get; set; }

        /// <summary>
        /// Horizontal
        /// </summary>
        [NameInMap("horizontal")]
        [Validation(Required=false)]
        public long? Horizontal { get; set; }

        /// <summary>
        /// Rotate
        /// </summary>
        [NameInMap("rotate")]
        [Validation(Required=false)]
        public double? Rotate { get; set; }

        /// <summary>
        /// Type
        /// </summary>
        [NameInMap("type")]
        [Validation(Required=false)]
        public int? Type { get; set; }

        /// <summary>
        /// Value
        /// </summary>
        [NameInMap("value")]
        [Validation(Required=false)]
        public string Value { get; set; }

        /// <summary>
        /// Vertical
        /// </summary>
        [NameInMap("vertical")]
        [Validation(Required=false)]
        public long? Vertical { get; set; }

    }

}
