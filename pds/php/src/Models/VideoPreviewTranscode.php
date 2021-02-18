<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

class VideoPreviewTranscode extends Model
{
    /**
     * @description status
     *
     * @example finished
     *
     * @var string
     */
    public $status;

    /**
     * @description template_id
     *
     * @example "Original"
     *
     * @var string
     */
    public $templateId;
    protected $_name = [
        'status'     => 'status',
        'templateId' => 'template_id',
    ];

    public function validate()
    {
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->status) {
            $res['status'] = $this->status;
        }
        if (null !== $this->templateId) {
            $res['template_id'] = $this->templateId;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return VideoPreviewTranscode
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['status'])) {
            $model->status = $map['status'];
        }
        if (isset($map['template_id'])) {
            $model->templateId = $map['template_id'];
        }

        return $model;
    }
}
