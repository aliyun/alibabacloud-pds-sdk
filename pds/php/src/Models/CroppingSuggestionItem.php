<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

class CroppingSuggestionItem extends Model
{
    /**
     * @var string
     */
    public $aspectRatio;

    /**
     * @var CroppingBoundary
     */
    public $croppingBoundary;

    /**
     * @var int
     */
    public $score;
    protected $_name = [
        'aspectRatio'      => 'aspect_ratio',
        'croppingBoundary' => 'cropping_boundary',
        'score'            => 'score',
    ];

    public function validate()
    {
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->aspectRatio) {
            $res['aspect_ratio'] = $this->aspectRatio;
        }
        if (null !== $this->croppingBoundary) {
            $res['cropping_boundary'] = null !== $this->croppingBoundary ? $this->croppingBoundary->toMap() : null;
        }
        if (null !== $this->score) {
            $res['score'] = $this->score;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return CroppingSuggestionItem
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['aspect_ratio'])) {
            $model->aspectRatio = $map['aspect_ratio'];
        }
        if (isset($map['cropping_boundary'])) {
            $model->croppingBoundary = CroppingBoundary::fromMap($map['cropping_boundary']);
        }
        if (isset($map['score'])) {
            $model->score = $map['score'];
        }

        return $model;
    }
}
